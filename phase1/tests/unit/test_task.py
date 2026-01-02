"""
Unit tests for the Task model to validate existing functionality.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task


def test_task_creation():
    """Test basic task creation with valid parameters."""
    task = Task(task_id=1, title="Test Task", description="Test Description", completed=False)

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed == False


def test_task_creation_defaults():
    """Test task creation with default values."""
    task = Task(task_id=2, title="Test Task 2")

    assert task.id == 2
    assert task.title == "Test Task 2"
    assert task.description == ""
    assert task.completed == False


def test_task_update_properties():
    """Test updating task properties."""
    task = Task(task_id=3, title="Original Title", description="Original Description", completed=False)

    task.title = "Updated Title"
    task.description = "Updated Description"
    task.completed = True

    assert task.title == "Updated Title"
    assert task.description == "Updated Description"
    assert task.completed == True


def test_task_to_dict():
    """Test converting task to dictionary."""
    task = Task(task_id=4, title="Test Task", description="Test Description", completed=True)
    task_dict = task.to_dict()

    assert task_dict["id"] == 4
    assert task_dict["title"] == "Test Task"
    assert task_dict["description"] == "Test Description"
    assert task_dict["completed"] == True


def test_task_from_dict():
    """Test creating task from dictionary."""
    data = {
        "id": 5,
        "title": "From Dict Task",
        "description": "From Dict Description",
        "completed": True
    }

    task = Task.from_dict(data)
    assert task.id == 5
    assert task.title == "From Dict Task"
    assert task.description == "From Dict Description"
    assert task.completed == True


def test_task_string_representation():
    """Test string representation of task."""
    task = Task(task_id=6, title="String Test", description="Description", completed=True)
    task_str = str(task)

    assert "✓" in task_str  # Check for completed indicator
    assert "ID: 6" in task_str
    assert "String Test" in task_str


def test_task_validation():
    """Test validation of task properties."""
    # Test valid creation
    task = Task(task_id=7, title="Valid Task")
    assert task.id == 7
    assert task.title == "Valid Task"

    # Test invalid ID
    try:
        Task(task_id="invalid", title="Invalid Task")
        assert False, "Should have raised ValueError for invalid ID"
    except ValueError:
        pass  # Expected

    # Test invalid title
    try:
        Task(task_id=8, title="")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected


if __name__ == "__main__":
    test_task_creation()
    test_task_creation_defaults()
    test_task_update_properties()
    test_task_to_dict()
    test_task_from_dict()
    test_task_string_representation()
    test_task_validation()
    print("All Task model tests passed!")