from sqlalchemy import Column, CheckConstraint, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, validates


class User(DeclarativeBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    __table_args__ = (CheckConstraint(age.between(0, 130)),)

    @validates("name")
    def validate_name(self, key, value):
        if len(value) == 0:
            raise ValueError("Name must not be empty")
        return value


class TimeRange(DeclarativeBase):
    __tablename__ = "time_range"
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    __table_args__ = (CheckConstraint(start_time > end_time),)
