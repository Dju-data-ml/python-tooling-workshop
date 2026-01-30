from src.models.task import Task, TaskStatus
from datetime import datetime

def test_task_creation():
    """Test that a task is created correctly."""
    now = datetime.now()
    task = Task(id=1, title="Test", description="Desc", status=TaskStatus.TODO, created_at=now)
    assert task.id == 1
    assert task.title == "Test"
    assert task.status == TaskStatus.TODO

def test_task_mark_done():
    """Test updating task status."""
    task = Task(id=1, title="Test", description="Desc", status=TaskStatus.TODO, created_at=datetime.now())
    task.status = TaskStatus.DONE
    assert task.status == TaskStatus.DONE
