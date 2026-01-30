"""Task manager service for managing tasks."""

from datetime import datetime
from typing import List, Optional

from src.models.task import Task, TaskStatus


class TaskManager:
    """
    Service for managing a collection of tasks.

    This class provides CRUD operations for tasks and maintains
    an in-memory list of tasks with auto-incrementing IDs.
    """

    def __init__(self) -> None:
        """Initialize the task manager with an empty task list."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """
        Create and add a new task.

        Args:
            title: Short description of the task
            description: Detailed description of what needs to be done

        Returns:
            The newly created task
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status=TaskStatus.TODO,
            created_at=datetime.now(),
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """
        List all tasks, optionally filtered by status.

        Args:
            status: If provided, only return tasks with this status

        Returns:
            List of tasks matching the criteria
        """
        if status is None:
            return self._tasks.copy()

        return [task for task in self._tasks if task.status == status]

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The unique identifier of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def update_task_status(self, task_id: int, status: TaskStatus) -> Optional[Task]:
        """
        Update the status of a task.

        Args:
            task_id: The unique identifier of the task
            status: The new status to set

        Returns:
            The updated task if found, None otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        task.status = status
        return task

    def count_tasks(self) -> int:
        """Return the total number of tasks."""
        return len(self._tasks)

    def count_by_status(self, status: TaskStatus) -> int:
        """
        Count tasks with a specific status.

        Args:
            status: The status to count

        Returns:
            Number of tasks with the given status
        """
        return len([task for task in self._tasks if task.status == status])
