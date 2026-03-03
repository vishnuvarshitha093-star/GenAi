from datetime import datetime, timezone

from fastapi import HTTPException, status

from app.models.enums import RequestStatus, RoleEnum
from app.models.request import ResourceRequest
from app.repositories.request_repository import RequestRepository
from app.schemas.request import RequestCreate, RequestUpdate
from app.services.audit_service import AuditService
from app.services.sla_service import SLAService


class RequestService:
    def __init__(self, repo: RequestRepository, audit_service: AuditService) -> None:
        self.repo = repo
        self.audit_service = audit_service

    def create(self, payload: RequestCreate, user_id: int) -> ResourceRequest:
        request_obj = ResourceRequest(
            title=payload.title,
            description=payload.description,
            category=payload.category,
            requested_by_id=user_id,
            due_date=SLAService.calculate_due_date(payload.category),
        )
        created = self.repo.create(request_obj)
        self.audit_service.capture(entity_type="request", entity_id=created.id, action="create", actor_id=user_id, old_value=None, new_value={"status": created.status.value})
        return created

    def update_submitted(self, request_id: int, payload: RequestUpdate, user_id: int) -> ResourceRequest:
        request_obj = self._get_or_404(request_id)
        if request_obj.status != RequestStatus.SUBMITTED:
            raise HTTPException(status_code=400, detail="Edits are allowed only in Submitted state")
        old = {"title": request_obj.title, "description": request_obj.description, "category": request_obj.category}
        for key, value in payload.model_dump(exclude_none=True).items():
            setattr(request_obj, key, value)
        updated = self.repo.save(request_obj)
        self.audit_service.capture(entity_type="request", entity_id=updated.id, action="update", actor_id=user_id, old_value=old, new_value=payload.model_dump(exclude_none=True))
        return updated

    def transition_status(self, request_id: int, target_status: RequestStatus, actor_id: int, actor_role: RoleEnum) -> ResourceRequest:
        request_obj = self._get_or_404(request_id)
        self._validate_transition(request_obj.status, target_status, actor_role)
        old_status = request_obj.status
        request_obj.status = target_status
        if target_status == RequestStatus.FULFILLED:
            request_obj.fulfilled_at = datetime.now(timezone.utc)
        if target_status == RequestStatus.CLOSED:
            request_obj.closed_at = datetime.now(timezone.utc)
        updated = self.repo.save(request_obj)
        self.audit_service.capture(entity_type="request", entity_id=updated.id, action="status_change", actor_id=actor_id, old_value={"status": old_status.value}, new_value={"status": target_status.value})
        return updated

    def list_requests(self) -> list[ResourceRequest]:
        return self.repo.list()

    def _get_or_404(self, request_id: int) -> ResourceRequest:
        request_obj = self.repo.get(request_id)
        if not request_obj:
            raise HTTPException(status_code=404, detail="Request not found")
        return request_obj

    @staticmethod
    def _validate_transition(current: RequestStatus, target: RequestStatus, role: RoleEnum) -> None:
        allowed = {
            RequestStatus.SUBMITTED: {RequestStatus.UNDER_REVIEW},
            RequestStatus.UNDER_REVIEW: {RequestStatus.APPROVED, RequestStatus.REJECTED},
            RequestStatus.APPROVED: {RequestStatus.FULFILLED},
            RequestStatus.FULFILLED: {RequestStatus.CLOSED},
        }
        if current == RequestStatus.CLOSED:
            raise HTTPException(status_code=400, detail="Closed requests are read-only")
        if target not in allowed.get(current, set()):
            raise HTTPException(status_code=400, detail=f"Invalid transition from {current} to {target}")
        if target == RequestStatus.FULFILLED and current != RequestStatus.APPROVED:
            raise HTTPException(status_code=400, detail="Only approved requests can be fulfilled")
        if target == RequestStatus.CLOSED and current != RequestStatus.FULFILLED:
            raise HTTPException(status_code=400, detail="Only fulfilled requests can be closed")
        if role not in {RoleEnum.APPROVER, RoleEnum.ADMIN} and target in {RequestStatus.UNDER_REVIEW, RequestStatus.APPROVED, RequestStatus.REJECTED, RequestStatus.FULFILLED, RequestStatus.CLOSED}:
            raise HTTPException(status_code=403, detail="Insufficient role")
