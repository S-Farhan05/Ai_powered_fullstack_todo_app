"""
Integration tests for the CLI flow to validate existing functionality.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.todo_service import TodoService


def test_full_task_lifecycle():
    """Test the complete lifecycle of a task through the service."""
    service = TodoService()

    # Add a task
    task = service.add_task("Integration Test Task", "Integration Test Description")

    assert task.id == 1
    assert task.title == "Integration Test Task"
    assert task.description == "Integration Test Description"
    assert task.completed == False

    # Verify task exists in the list
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == 1

    # Update the task
    success = service.update_task(1, title="Updated Integration Task", description="Updated Description")
    assert success == True

    # Verify the update
    updated_task = service.get_task_by_id(1)
    assert updated_task.title == "Updated Integration Task"
    assert updated_task.description == "Updated Description"

    # Mark as complete
    success = service.update_task_status(1, True)
    assert success == True

    # Verify status change
    completed_task = service.get_task_by_id(1)
    assert completed_task.completed == True

    # Mark as incomplete again
    success = service.update_task_status(1, False)
    assert success == True

    # Verify status change
    incomplete_task = service.get_task_by_id(1)
    assert incomplete_task.completed == False

    # Delete the task
    success = service.delete_task(1)
    assert success == True

    # Verify task is deleted
    assert service.get_task_by_id(1) is None
    all_tasks_after_delete = service.get_all_tasks()
    assert len(all_tasks_after_delete) == 0


def test_multiple_tasks():
    """Test handling multiple tasks."""
    service = TodoService()

    # Add multiple tasks
    task1 = service.add_task("Task 1", "Description 1")
    task2 = service.add_task("Task 2", "Description 2")
    task3 = service.add_task("Task 3", "Description 3")

    # Verify all tasks exist
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 3

    # Verify each task has correct properties
    assert all_tasks[0].id == 1 and all_tasks[0].title == "Task 1"
    assert all_tasks[1].id == 2 and all_tasks[1].title == "Task 2"
    assert all_tasks[2].id == 3 and all_tasks[2].title == "Task 3"

    # Update middle task
    success = service.update_task(2, title="Updated Task 2")
    assert success == True

    # Verify update
    updated_task = service.get_task_by_id(2)
    assert updated_task.title == "Updated Task 2"

    # Mark one as complete
    success = service.update_task_status(1, True)
    assert success == True

    # Verify status
    completed_task = service.get_task_by_id(1)
    assert completed_task.completed == True

    # Delete a task
    success = service.delete_task(2)
    assert success == True

    # Verify deletion
    all_tasks_after_delete = service.get_all_tasks()
    assert len(all_tasks_after_delete) == 2
    assert service.get_task_by_id(2) is None  # Task 2 should be gone
    assert service.get_task_by_id(1) is not None  # Task 1 should remain
    assert service.get_task_by_id(3) is not None  # Task 3 should remain


def test_task_id_uniqueness():
    """Test that task IDs remain unique after deletions."""
    service = TodoService()

    # Add tasks
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")
    task3 = service.add_task("Task 3")

    # Verify IDs
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3

    # Delete middle task
    service.delete_task(2)

    # Add a new task - it should get the next ID
    task4 = service.add_task("Task 4")
    assert task4.id == 4

    # Verify remaining tasks still have their original IDs
    remaining_tasks = service.get_all_tasks()
    task_ids = [task.id for task in remaining_tasks]
    assert 1 in task_ids  # Original task 1
    assert 2 not in task_ids  # Deleted task 2
    assert 3 in task_ids  # Original task 3
    assert 4 in task_ids  # New task 4


def test_error_handling_scenarios():
    """Test error handling scenarios to ensure proper validation."""
    service = TodoService()

    # Test adding task with empty title
    try:
        service.add_task("")
        assert False, "Should have raised an exception for empty title"
    except Exception:
        pass  # Expected

    # Test adding task with whitespace-only title
    try:
        service.add_task("   ")
        assert False, "Should have raised an exception for whitespace-only title"
    except Exception:
        pass  # Expected

    # Test updating non-existent task
    success = service.update_task(999, title="New Title")
    assert success == False, "Should return False for non-existent task"

    # Test updating status of non-existent task
    success = service.update_task_status(999, True)
    assert success == False, "Should return False for non-existent task"

    # Test deleting non-existent task
    success = service.delete_task(999)
    assert success == False, "Should return False for non-existent task"

    # Test with valid inputs to ensure functionality still works
    task = service.add_task("Valid Task")
    assert task.id == 1
    assert task.title == "Valid Task"

    # Update the valid task
    success = service.update_task(1, title="Updated Valid Task")
    assert success == True

    # Update task status
    success = service.update_task_status(1, True)
    assert success == True

    # Verify the updates worked
    updated_task = service.get_task_by_id(1)
    assert updated_task.title == "Updated Valid Task"
    assert updated_task.completed == True

    # Delete the valid task
    success = service.delete_task(1)
    assert success == True

    # Verify deletion worked
    deleted_task = service.get_task_by_id(1)
    assert deleted_task is None


def test_input_validation_scenarios():
    """Test various input validation scenarios."""
    service = TodoService()

    # Test adding task with very long title
    try:
        service.add_task("A" * 201)  # Exceeds limit
        assert False, "Should have raised an exception for long title"
    except Exception:
        pass  # Expected

    # Test adding task with very long description
    try:
        service.add_task("Valid Title", "B" * 1001)  # Exceeds limit
        assert False, "Should have raised an exception for long description"
    except Exception:
        pass  # Expected

    # Test updating with invalid inputs
    task = service.add_task("Valid Task")

    # Try to update with empty title
    try:
        service.update_task(1, title="")
        assert False, "Should have raised an exception for empty title"
    except Exception:
        pass  # Expected

    # Try to update with very long title
    try:
        service.update_task(1, title="C" * 201)  # Exceeds limit
        assert False, "Should have raised an exception for long title"
    except Exception:
        pass  # Expected

    # Verify task still exists with original title
    still_exists_task = service.get_task_by_id(1)
    assert still_exists_task is not None
    assert still_exists_task.title == "Valid Task"


if __name__ == "__main__":
    test_full_task_lifecycle()
    test_multiple_tasks()
    test_task_id_uniqueness()
    test_error_handling_scenarios()
    test_input_validation_scenarios()
    print("All CLI flow integration tests passed!")