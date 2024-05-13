from pydantic import BaseModel, model_validator
from datetime import datetime


class TimeRange(BaseModel):
    start_at: datetime
    end_at: datetime

    @model_validator(mode="after")
    def validate_time_range(self):
        if self.start_at > self.end_at:
            raise ValueError("end_at must not be before start_at")

    class Config:
        frozen = True


TimeRange.model_json_schema()


def get_meetings(user_id: int, time_range: TimeRange):
    pass
