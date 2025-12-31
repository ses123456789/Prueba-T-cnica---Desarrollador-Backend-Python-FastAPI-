from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True  # SQLAlchemy → Pydantic
