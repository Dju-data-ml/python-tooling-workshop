"""Task model for the task manager application."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    """Enumeration of possible task statuses."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """
    Represents a task in the task manager.

    Attributes:
        id: Unique identifier for the task
        title: Short description of the task
        description: Detailed description of what needs to be done
        status: Current status of the task
        created_at: Timestamp when the task was created
    """

    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime

    def mark_in_progress(self) -> None:
        """Mark the task as in progress."""
        self.status = TaskStatus.IN_PROGRESS

    def mark_done(self) -> None:
        """Mark the task as completed."""
        self.status = TaskStatus.DONE

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        return f"Task #{self.id}: {self.title} [{self.status.value}]"
