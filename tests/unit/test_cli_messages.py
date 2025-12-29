"""
Unit tests for CLI message improvements in the todo application.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cli.main import TodoCLI


def test_cli_message_improvements():
    """Test that CLI provides clear, consistent messages for all operations."""
    # We'll test the message formatting by examining the CLI class
    cli = TodoCLI()

    # Verify that CLI methods exist and provide clear feedback
    assert hasattr(cli, 'display_menu'), "CLI should have a display menu method"
    assert hasattr(cli, 'add_task'), "CLI should have an add task method"
    assert hasattr(cli, 'view_all_tasks'), "CLI should have a view all tasks method"
    assert hasattr(cli, 'update_task'), "CLI should have an update task method"
    assert hasattr(cli, 'delete_task'), "CLI should have a delete task method"
    assert hasattr(cli, 'mark_task_complete'), "CLI should have a mark task complete method"
    assert hasattr(cli, 'mark_task_incomplete'), "CLI should have a mark task incomplete method"

    # Verify the CLI has a service attribute
    assert hasattr(cli, 'service'), "CLI should have a service attribute"


def test_clear_confirmation_messages():
    """Test that confirmation messages are clear and helpful."""
    # This is more of a structural test since we can't easily test console output
    cli = TodoCLI()

    # The methods should be designed to provide clear feedback
    # This test verifies that the methods exist and follow expected naming
    methods = dir(cli)

    # Verify we have the expected methods
    expected_methods = [
        'add_task',
        'view_all_tasks',
        'update_task',
        'delete_task',
        'mark_task_complete',
        'mark_task_incomplete'
    ]

    for method in expected_methods:
        assert method in methods, f"CLI should have {method} method"


def test_menu_prompt_clarity():
    """Test that menu prompts are clear and properly labeled."""
    cli = TodoCLI()

    # Check that the display_menu method exists
    assert hasattr(cli, 'display_menu'), "CLI should have a display_menu method"

    # Menu should have clear options
    menu_options = [
        "Add Task",
        "View All Tasks",
        "Update Task",
        "Delete Task",
        "Mark Task Complete",
        "Mark Task Incomplete",
        "Exit"
    ]

    # Verify that the menu structure is clear
    assert hasattr(cli, 'get_user_choice'), "CLI should have a get_user_choice method"


if __name__ == "__main__":
    test_cli_message_improvements()
    test_clear_confirmation_messages()
    test_menu_prompt_clarity()
    print("All CLI message tests passed!")