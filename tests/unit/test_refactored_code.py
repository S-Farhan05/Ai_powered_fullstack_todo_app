"""
Unit tests for refactored code functionality in the todo application.
This ensures that all refactored code maintains the same functionality.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task
from src.services.todo_service import TodoService
from src.cli.main import TodoCLI


def test_task_model_functionality():
    """Test that the Task model maintains all expected functionality after refactoring."""
    # Test basic creation
    task = Task(task_id=1, title="Test Task", description="Test Description", completed=False)

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed == False

    # Test updating properties
    task.title = "Updated Title"
    task.description = "Updated Description"
    task.completed = True

    assert task.title == "Updated Title"
    assert task.description == "Updated Description"
    assert task.completed == True

    # Test to_dict and from_dict
    task_dict = task.to_dict()
    assert task_dict["id"] == 1
    assert task_dict["title"] == "Updated Title"
    assert task_dict["description"] == "Updated Description"
    assert task_dict["completed"] == True

    reconstructed_task = Task.from_dict(task_dict)
    assert reconstructed_task.id == 1
    assert reconstructed_task.title == "Updated Title"
    assert reconstructed_task.description == "Updated Description"
    assert reconstructed_task.completed == True

    # Test validation
    try:
        invalid_task = Task(task_id=-1, title="Invalid")
        assert False, "Should have raised ValueError for invalid ID"
    except ValueError:
        pass  # Expected

    try:
        invalid_task = Task(task_id=1, title="")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected


def test_todo_service_functionality():
    """Test that the TodoService maintains all expected functionality after refactoring."""
    service = TodoService()

    # Test initial state
    assert len(service.get_all_tasks()) == 0
    assert service.next_id == 1

    # Test adding tasks
    task1 = service.add_task("Task 1", "Description 1")
    assert task1.id == 1
    assert task1.title == "Task 1"
    assert task1.description == "Description 1"
    assert task1.completed == False

    task2 = service.add_task("Task 2", "Description 2")
    assert task2.id == 2

    # Test getting all tasks
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 2

    # Test getting specific task
    retrieved_task = service.get_task_by_id(1)
    assert retrieved_task is not None
    assert retrieved_task.title == "Task 1"

    # Test updating task
    success = service.update_task(1, title="Updated Task 1", description="Updated Description 1")
    assert success == True

    updated_task = service.get_task_by_id(1)
    assert updated_task.title == "Updated Task 1"
    assert updated_task.description == "Updated Description 1"

    # Test updating task status
    success = service.update_task_status(1, True)
    assert success == True

    status_updated_task = service.get_task_by_id(1)
    assert status_updated_task.completed == True

    # Test deleting task
    success = service.delete_task(2)
    assert success == True

    deleted_task = service.get_task_by_id(2)
    assert deleted_task is None

    remaining_tasks = service.get_all_tasks()
    assert len(remaining_tasks) == 1


def test_cli_structure():
    """Test that the CLI maintains proper structure and functionality after refactoring."""
    cli = TodoCLI()

    # Test that CLI has the expected service
    assert hasattr(cli, 'service')
    assert cli.service is not None

    # Test that CLI has all expected methods
    expected_methods = [
        'display_menu',
        'get_user_choice',
        'add_task',
        'view_all_tasks',
        'update_task',
        'delete_task',
        'mark_task_complete',
        'mark_task_incomplete',
        'run'
    ]

    for method in expected_methods:
        assert hasattr(cli, method), f"CLI should have {method} method"


def test_separation_of_concerns():
    """Test that proper separation of concerns is maintained after refactoring."""
    # Test that models, services, and CLI components are properly separated
    from src.models.task import Task
    from src.services.todo_service import TodoService
    from src.cli.main import TodoCLI

    # Verify that each component has its own responsibility
    task = Task(task_id=1, title="Test", description="Description")

    service = TodoService()
    added_task = service.add_task("Service Test", "Service Description")

    cli = TodoCLI()

    # Each component should have its own specific functionality
    assert hasattr(task, 'id') and hasattr(task, 'title')
    assert hasattr(service, 'add_task') and hasattr(service, 'get_all_tasks')
    assert hasattr(cli, 'display_menu') and hasattr(cli, 'run')


def test_consistent_formatting_and_naming():
    """Test that consistent formatting and naming conventions are maintained."""
    # This tests that the refactored code maintains consistent conventions
    service = TodoService()

    # Add a task and verify it follows naming conventions
    task = service.add_task("Consistent Naming Test", "Test for consistent naming")

    # Verify the task was created properly
    assert task.title == "Consistent Naming Test"
    assert task.description == "Test for consistent naming"

    # Test that property accessors work consistently
    assert hasattr(task, 'id')
    assert hasattr(task, 'title')
    assert hasattr(task, 'description')
    assert hasattr(task, 'completed')


if __name__ == "__main__":
    test_task_model_functionality()
    test_todo_service_functionality()
    test_cli_structure()
    test_separation_of_concerns()
    test_consistent_formatting_and_naming()
    print("All refactored code functionality tests passed!")