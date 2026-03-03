import pytest
from fastapi import HTTPException

from app.models.enums import RequestStatus, RoleEnum
from app.services.request_service import RequestService


def test_invalid_transition_rejected_to_fulfilled() -> None:
    with pytest.raises(HTTPException):
        RequestService._validate_transition(RequestStatus.REJECTED, RequestStatus.FULFILLED, RoleEnum.APPROVER)
