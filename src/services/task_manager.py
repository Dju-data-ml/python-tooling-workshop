"""Task manager service for managing tasks."""

import json
from datetime import datetime
from pathlib import Path
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
        self._file_path = Path("tasks.json")
        self._load_tasks()

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
        self._save_tasks()
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

    def _load_tasks(self) -> None:
        """Load tasks from JSON file if it exists."""
        if self._file_path.exists():
            try:
                with open(self._file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for task_data in data:
                        task = Task(
                            id=task_data['id'],
                            title=task_data['title'],
                            description=task_data['description'],
                            status=TaskStatus(task_data['status']),
                            created_at=datetime.fromisoformat(task_data['created_at'])
                        )
                        self._tasks.append(task)
                        self._next_id = max(self._next_id, task.id + 1)
            except (json.JSONDecodeError, KeyError, ValueError):
                # If file is corrupted, start fresh
                pass

    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        data = []
        for task in self._tasks:
            data.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status.value,
                'created_at': task.created_at.isoformat()
            })
        with open(self._file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
