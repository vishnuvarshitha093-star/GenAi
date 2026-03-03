from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.request import ResourceRequest


class RequestRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> list[ResourceRequest]:
        return list(self.db.scalars(select(ResourceRequest).order_by(ResourceRequest.created_at.desc())))

    def get(self, request_id: int) -> ResourceRequest | None:
        return self.db.get(ResourceRequest, request_id)

    def create(self, request_obj: ResourceRequest) -> ResourceRequest:
        self.db.add(request_obj)
        self.db.commit()
        self.db.refresh(request_obj)
        return request_obj

    def save(self, request_obj: ResourceRequest) -> ResourceRequest:
        self.db.add(request_obj)
        self.db.commit()
        self.db.refresh(request_obj)
        return request_obj
