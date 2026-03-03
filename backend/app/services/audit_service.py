import json

from app.models.audit_log import AuditLog
from app.repositories.audit_repository import AuditRepository


class AuditService:
    def __init__(self, repo: AuditRepository) -> None:
        self.repo = repo

    def capture(self, *, entity_type: str, entity_id: int, action: str, actor_id: int, old_value: dict | None, new_value: dict | None) -> None:
        self.repo.log(
            AuditLog(
                entity_type=entity_type,
                entity_id=entity_id,
                action=action,
                actor_id=actor_id,
                old_value=json.dumps(old_value) if old_value else None,
                new_value=json.dumps(new_value) if new_value else None,
            )
        )
