import pytest
import os
from src.services.task_manager import TaskManager
from src.models.task import TaskStatus

@pytest.fixture
def manager():
    """Fixture to provide a clean TaskManager for each test."""
    # Use a temporary file for tests to avoid messing with real data
    test_file = "tasks_test.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    m = TaskManager()
    m._file_path = m._file_path.with_name(test_file)
    # Clear tasks for a clean start
    m._tasks = []
    m._next_id = 1
    
    yield m
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_task(manager):
    """Test adding a task."""
    task = manager.add_task("Test Task", "Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert len(manager.list_tasks()) == 1

def test_list_tasks_filtering(manager):
    """Test filtering tasks by status."""
    manager.add_task("Task 1", "Desc 1")
    t2 = manager.add_task("Task 2", "Desc 2")
    manager.update_task_status(t2.id, TaskStatus.DONE)
    
    all_tasks = manager.list_tasks()
    todo_tasks = manager.list_tasks(status=TaskStatus.TODO)
    done_tasks = manager.list_tasks(status=TaskStatus.DONE)
    
    assert len(all_tasks) == 2
    assert len(todo_tasks) == 1
    assert len(done_tasks) == 1

def test_delete_task(manager):
    """Test deleting a task."""
    task = manager.add_task("To Delete", "Desc")
    assert manager.delete_task(task.id) is True
    assert len(manager.list_tasks()) == 0
    assert manager.delete_task(999) is False

def test_update_status(manager):
    """Test updating task status."""
    task = manager.add_task("To Update", "Desc")
    updated_task = manager.update_task_status(task.id, TaskStatus.IN_PROGRESS)
    assert updated_task.status == TaskStatus.IN_PROGRESS
    assert manager.get_task(task.id).status == TaskStatus.IN_PROGRESS
