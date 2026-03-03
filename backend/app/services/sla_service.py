from datetime import datetime, timedelta, timezone


class SLAService:
    SLA_BY_CATEGORY_HOURS = {
        "system_access": 24,
        "equipment": 72,
        "facility": 48,
    }

    @classmethod
    def calculate_due_date(cls, category: str) -> datetime:
        hours = cls.SLA_BY_CATEGORY_HOURS.get(category, 48)
        return datetime.now(timezone.utc) + timedelta(hours=hours)
