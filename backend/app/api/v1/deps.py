from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.audit_repository import AuditRepository
from app.repositories.request_repository import RequestRepository
from app.repositories.user_repository import UserRepository
from app.services.audit_service import AuditService
from app.services.auth_service import AuthService
from app.services.request_service import RequestService


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


def get_request_service(db: Session = Depends(get_db)) -> RequestService:
    audit = AuditService(AuditRepository(db))
    return RequestService(RequestRepository(db), audit)
