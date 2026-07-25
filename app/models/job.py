from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(255))

    company: Mapped[str] = mapped_column(String(255))

    location: Mapped[str] = mapped_column(String(255))

    salary: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str] = mapped_column(Text)

    url: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )

    source: Mapped[str] = mapped_column(String(100))

    match_score: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    applied: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )