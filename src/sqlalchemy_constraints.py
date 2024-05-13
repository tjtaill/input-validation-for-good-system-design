from sqlalchemy import (
    Table,
    Column,
    CheckConstraint,
    Integer,
    String,
    DateTime,
    MetaData,
)

meta_data = MetaData()

User2 = Table(
    "user2",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("age", Integer, CheckConstraint("age > 0 AND age < 130"), nullable=False),
    Column("name", String(50), CheckConstraint("LENGTH(name) > 0"), nullable=False),
)

TimeRange2 = Table(
    "time_range2",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("start_time", DateTime, nullable=False),
    Column("end_time", DateTime, nullable=False),
    CheckConstraint("start_time > end_time"),
)
