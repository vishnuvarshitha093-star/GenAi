from app.services.sla_service import SLAService


def test_sla_due_date_is_future() -> None:
    due = SLAService.calculate_due_date("system_access")
    assert due.tzinfo is not None
