from enum import StrEnum


class RoleEnum(StrEnum):
    USER = "User"
    APPROVER = "Approver"
    ADMIN = "Admin"


class RequestStatus(StrEnum):
    SUBMITTED = "Submitted"
    UNDER_REVIEW = "Under Review"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    FULFILLED = "Fulfilled"
    CLOSED = "Closed"
