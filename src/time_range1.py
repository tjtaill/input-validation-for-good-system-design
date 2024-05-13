from datetime import datetime


def get_meetings(user_id: int, start_at: str, end_at: str):
    start_dt = datetime.fromisoformat(start_at)
    end_dt = datetime.fromisoformat(end_at)
    if start_dt > end_dt:
        raise ValueError("end_at must not be before start_at")


def get_meetings2(user_id: int, start_at: datetime, end_at: datetime):
    if start_at > end_at:
        raise ValueError("end_at must not be before start_at")
