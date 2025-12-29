"""
Unit tests for the TodoService to validate existing functionality.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.todo_service import TodoService


def test_todo_service_initialization():
    """Test TodoService initialization."""
    service = TodoService()

    assert len(service.get_all_tasks()) == 0
    assert service.next_id == 1


def test_add_task():
    """Test adding a new task."""
    service = TodoService()

    task = service.add_task("Test Task", "Test Description")

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed == False

    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1


def test_get_all_tasks():
    """Test retrieving all tasks."""
    service = TodoService()

    # Add multiple tasks
    service.add_task("Task 1", "Description 1")
    service.add_task("Task 2", "Description 2")

    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2


def test_get_task_by_id():
    """Test retrieving a specific task by ID."""
    service = TodoService()

    # Add tasks
    service.add_task("Task 1", "Description 1")
    service.add_task("Task 2", "Description 2")

    # Get existing task
    task = service.get_task_by_id(1)
    assert task is not None
    assert task.id == 1
    assert task.title == "Task 1"

    # Get non-existing task
    task = service.get_task_by_id(999)
    assert task is None


def test_update_task():
    """Test updating task details."""
    service = TodoService()

    # Add a task
    service.add_task("Original Title", "Original Description")

    # Update the task
    success = service.update_task(1, title="Updated Title", description="Updated Description")

    assert success == True

    task = service.get_task_by_id(1)
    assert task.title == "Updated Title"
    assert task.description == "Updated Description"


def test_update_task_partial():
    """Test updating only title or description."""
    service = TodoService()

    # Add a task
    service.add_task("Original Title", "Original Description")

    # Update only title
    success = service.update_task(1, title="Updated Title")

    assert success == True

    task = service.get_task_by_id(1)
    assert task.title == "Updated Title"
    assert task.description == "Original Description"


def test_update_nonexistent_task():
    """Test updating a non-existent task."""
    service = TodoService()

    success = service.update_task(999, title="Updated Title")

    assert success == False


def test_update_task_status():
    """Test updating task completion status."""
    service = TodoService()

    # Add a task
    service.add_task("Test Task")

    # Mark as complete
    success = service.update_task_status(1, True)

    assert success == True

    task = service.get_task_by_id(1)
    assert task.completed == True


def test_update_task_status_nonexistent():
    """Test updating status of non-existent task."""
    service = TodoService()

    success = service.update_task_status(999, True)

    assert success == False


def test_delete_task():
    """Test deleting a task."""
    service = TodoService()

    # Add tasks
    service.add_task("Task 1")
    service.add_task("Task 2")

    # Delete first task
    success = service.delete_task(1)

    assert success == True

    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert service.get_task_by_id(1) is None
    assert service.get_task_by_id(2) is not None


def test_delete_nonexistent_task():
    """Test deleting a non-existent task."""
    service = TodoService()

    success = service.delete_task(999)

    assert success == False


def test_id_generation():
    """Test unique ID generation."""
    service = TodoService()

    # Add several tasks
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")
    task3 = service.add_task("Task 3")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3

    # Delete middle task and add another
    service.delete_task(2)
    task4 = service.add_task("Task 4")

    assert task4.id == 4  # Should continue the sequence


def test_error_handling_add_task():
    """Test error handling when adding tasks with invalid inputs."""
    service = TodoService()

    # Test adding task with empty title
    try:
        service.add_task("")
        assert False, "Should have raised InvalidTaskInputError for empty title"
    except Exception:
        pass  # Expected

    # Test adding task with whitespace-only title
    try:
        service.add_task("   ")
        assert False, "Should have raised InvalidTaskInputError for whitespace-only title"
    except Exception:
        pass  # Expected

    # Test adding task with very long title
    try:
        service.add_task("A" * 201)  # Exceeds limit
        assert False, "Should have raised InvalidTaskInputError for long title"
    except Exception:
        pass  # Expected

    # Test adding task with very long description
    try:
        service.add_task("Valid Title", "A" * 1001)  # Exceeds limit
        assert False, "Should have raised InvalidTaskInputError for long description"
    except Exception:
        pass  # Expected


def test_error_handling_update_task():
    """Test error handling when updating non-existent tasks."""
    service = TodoService()

    # Try to update a non-existent task
    success = service.update_task(999, title="New Title")
    assert success == False, "Should return False for non-existent task"


def test_error_handling_update_task_invalid_input():
    """Test error handling when updating tasks with invalid inputs."""
    service = TodoService()

    # Add a valid task first
    task = service.add_task("Original Title")

    # Try to update with empty title
    try:
        service.update_task(1, title="")
        assert False, "Should have raised InvalidTaskInputError for empty title"
    except Exception:
        pass  # Expected

    # Try to update with whitespace-only title
    try:
        service.update_task(1, title="   ")
        assert False, "Should have raised InvalidTaskInputError for whitespace-only title"
    except Exception:
        pass  # Expected


def test_error_handling_update_task_status():
    """Test error handling when updating status of non-existent tasks."""
    service = TodoService()

    # Try to update status of a non-existent task
    success = service.update_task_status(999, True)
    assert success == False, "Should return False for non-existent task"

    # Try to update status with invalid type
    try:
        service.update_task_status(1, "invalid")
        assert False, "Should have raised InvalidTaskInputError for invalid status type"
    except Exception:
        pass  # Expected


def test_error_handling_delete_task():
    """Test error handling when deleting non-existent tasks."""
    service = TodoService()

    # Try to delete a non-existent task
    success = service.delete_task(999)
    assert success == False, "Should return False for non-existent task"


if __name__ == "__main__":
    test_todo_service_initialization()
    test_add_task()
    test_get_all_tasks()
    test_get_task_by_id()
    test_update_task()
    test_update_task_partial()
    test_update_nonexistent_task()
    test_update_task_status()
    test_update_task_status_nonexistent()
    test_delete_task()
    test_delete_nonexistent_task()
    test_id_generation()
    test_error_handling_add_task()
    test_error_handling_update_task()
    test_error_handling_update_task_invalid_input()
    test_error_handling_update_task_status()
    test_error_handling_delete_task()
    print("All TodoService tests passed!")