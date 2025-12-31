from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Index
from sqlalchemy.sql import func
from app.db.base import Base
import enum


class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        Enum(TaskStatus, name="task_status"),
        nullable=False,
        default=TaskStatus.pending
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )



Index("ix_tasks_status", Task.status)
Index("ix_tasks_created_at", Task.created_at)
