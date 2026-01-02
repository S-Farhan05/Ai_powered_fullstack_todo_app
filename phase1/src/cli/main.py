"""
Main CLI interface for the todo application.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from services.todo_service import TodoService
from services.exceptions import TaskNotFoundError, InvalidTaskInputError
from utils.validation import validate_numeric_input, is_empty_or_whitespace_only, sanitize_input


class TodoCLI:
    """
    Command-line interface for the todo application.
    """

    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()

    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("0. Exit")
        print("="*50)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            str: The user's choice as a string
        """
        try:
            choice = input("Enter your choice (0-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            return "0"

    def add_task(self):
        """
        Add a new task to the system.
        """
        print("\n--- Add New Task ---")
        title_input = input("Enter task title: ")
        title = sanitize_input(title_input)

        if is_empty_or_whitespace_only(title):
            print("Error: Title cannot be empty or contain only whitespace.")
            return

        description_input = input("Enter task description (optional): ")
        description = sanitize_input(description_input)

        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except InvalidTaskInputError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    def view_all_tasks(self):
        """
        View all tasks in the system.
        """
        print("\n--- All Tasks ---")
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"[{status}] ID: {task.id} | Title: {task.title} | Description: {task.description}")

    def update_task(self):
        """
        Update an existing task's title or description.
        """
        print("\n--- Update Task ---")

        task_id_input = input("Enter task ID to update: ")
        task_id_str = sanitize_input(task_id_input)

        if not validate_numeric_input(task_id_str):
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        try:
            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return
        except Exception as e:
            print(f"Error: An error occurred while retrieving the task: {e}")
            return

        print(f"Current task: [{ '✓' if task.completed else '○' }] {task.title}")

        new_title_input = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ")
        new_title = sanitize_input(new_title_input) if new_title_input.strip() else None

        new_description_input = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ")
        new_description = sanitize_input(new_description_input) if new_description_input.strip() else None

        # If user entered the same as current, treat as no change
        if new_title == task.title:
            new_title = None
        if new_description == task.description:
            new_description = None

        try:
            success = self.service.update_task(task_id, new_title, new_description)

            if success:
                print("Task updated successfully!")
            else:
                print("Error: Failed to update task.")
        except InvalidTaskInputError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    def delete_task(self):
        """
        Delete a task by its ID.
        """
        print("\n--- Delete Task ---")

        task_id_input = input("Enter task ID to delete: ")
        task_id_str = sanitize_input(task_id_input)

        if not validate_numeric_input(task_id_str):
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        try:
            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return
        except Exception as e:
            print(f"Error: An error occurred while retrieving the task: {e}")
            return

        print(f"Task to delete: [{ '✓' if task.completed else '○' }] {task.title}")

        confirm = input("Are you sure you want to delete this task? (y/N): ")
        confirm_clean = sanitize_input(confirm).lower()

        if confirm_clean in ['y', 'yes']:
            try:
                success = self.service.delete_task(task_id)
                if success:
                    print("Task deleted successfully!")
                else:
                    print("Error: Failed to delete task.")
            except Exception as e:
                print(f"Error: An error occurred while deleting the task: {e}")
        else:
            print("Delete operation cancelled.")

    def mark_task_complete(self):
        """
        Mark a task as complete.
        """
        print("\n--- Mark Task Complete ---")

        task_id_input = input("Enter task ID to mark complete: ")
        task_id_str = sanitize_input(task_id_input)

        if not validate_numeric_input(task_id_str):
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        try:
            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return
        except Exception as e:
            print(f"Error: An error occurred while retrieving the task: {e}")
            return

        try:
            success = self.service.update_task_status(task_id, True)

            if success:
                print(f"Task '{task.title}' marked as complete!")
            else:
                print("Error: Failed to update task status.")
        except InvalidTaskInputError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    def mark_task_incomplete(self):
        """
        Mark a task as incomplete.
        """
        print("\n--- Mark Task Incomplete ---")

        task_id_input = input("Enter task ID to mark incomplete: ")
        task_id_str = sanitize_input(task_id_input)

        if not validate_numeric_input(task_id_str):
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        try:
            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return
        except Exception as e:
            print(f"Error: An error occurred while retrieving the task: {e}")
            return

        try:
            success = self.service.update_task_status(task_id, False)

            if success:
                print(f"Task '{task.title}' marked as incomplete!")
            else:
                print("Error: Failed to update task status.")
        except InvalidTaskInputError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    def run(self):
        """
        Run the main application loop.
        """
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "0":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 6.")

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")


def main():
    """
    Main function to run the todo application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()