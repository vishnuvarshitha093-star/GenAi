from datetime import datetime

from pydantic import BaseModel, Field

from app.models.enums import RequestStatus


class RequestCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str
    category: str


class RequestUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None


class RequestStatusUpdate(BaseModel):
    status: RequestStatus


class RequestResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    status: RequestStatus
    due_date: datetime
    requested_by_id: int

    class Config:
        from_attributes = True
