from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def log(self, entry: AuditLog) -> None:
        self.db.add(entry)
        self.db.commit()
