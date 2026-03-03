from fastapi import APIRouter, Depends
from fastapi.responses import Response

from app.api.v1.deps import get_request_service
from app.middleware.auth import CurrentUser, get_current_user
from app.models.enums import RoleEnum
from app.schemas.request import RequestCreate, RequestResponse, RequestStatusUpdate, RequestUpdate
from app.services.request_service import RequestService
from app.utils.exporters import export_requests_csv, export_requests_excel, export_requests_pdf

router = APIRouter(prefix="/requests", tags=["requests"])


@router.post("", response_model=RequestResponse)
def create_request(payload: RequestCreate, user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> RequestResponse:
    return service.create(payload, user.user_id)


@router.patch("/{request_id}", response_model=RequestResponse)
def update_request(request_id: int, payload: RequestUpdate, user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> RequestResponse:
    return service.update_submitted(request_id, payload, user.user_id)


@router.post("/{request_id}/status", response_model=RequestResponse)
def update_request_status(request_id: int, payload: RequestStatusUpdate, user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> RequestResponse:
    return service.transition_status(request_id, payload.status, user.user_id, user.role)


@router.get("", response_model=list[RequestResponse])
def list_requests(user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> list[RequestResponse]:
    _ = user
    return service.list_requests()


@router.get("/exports/csv")
def export_csv(user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> Response:
    _ = user
    return Response(content=export_requests_csv(service.list_requests()), media_type="text/csv")


@router.get("/exports/excel")
def export_excel(user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> Response:
    _ = user
    return Response(content=export_requests_excel(service.list_requests()), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@router.get("/exports/pdf")
def export_pdf(user: CurrentUser = Depends(get_current_user), service: RequestService = Depends(get_request_service)) -> Response:
    _ = user
    return Response(content=export_requests_pdf(service.list_requests()), media_type="application/pdf")
