"""
TodoService provides business logic for managing tasks in memory.
"""

from typing import List, Optional
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.task import Task
from .exceptions import TaskNotFoundError, InvalidTaskInputError


class TodoService:
    """
    Service class for managing tasks with in-memory storage.
    """

    def __init__(self):
        """
        Initialize the TodoService with empty task list and ID counter.
        """
        self._tasks: List[Task] = []
        self._next_id = 1

    def _validate_task_exists(self, task_id: int) -> Task:
        """
        Validate that a task with the given ID exists.

        Args:
            task_id (int): The ID of the task to check

        Returns:
            Task: The task if found

        Raises:
            TaskNotFoundError: If the task does not exist
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        return task

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.

        Args:
            title (str): The title of the task
            description (str): The description of the task (optional)

        Returns:
            Task: The newly created task with unique ID and 'incomplete' status

        Raises:
            InvalidTaskInputError: If the title is empty or invalid
        """
        # Validate inputs before creating task
        if not title or title.strip() == "":
            raise InvalidTaskInputError("Title cannot be empty or whitespace-only")

        try:
            task = Task(
                task_id=self._next_id,
                title=title,
                description=description,
                completed=False  # Default to incomplete
            )
        except ValueError as e:
            raise InvalidTaskInputError(f"Invalid task input: {str(e)}")

        self._tasks.append(task)
        self._next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List[Task]: A list of all tasks
        """
        return self._tasks.copy()  # Return a copy to prevent external modification

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title for the task (if provided)
            description (Optional[str]): New description for the task (if provided)

        Returns:
            bool: True if the task was updated, False if task was not found

        Raises:
            InvalidTaskInputError: If the provided title or description is invalid
        """
        try:
            task = self._validate_task_exists(task_id)
        except TaskNotFoundError:
            return False

        # Validate inputs before updating
        if title is not None:
            try:
                task.title = title
            except ValueError as e:
                raise InvalidTaskInputError(f"Invalid title: {str(e)}")

        if description is not None:
            try:
                task.description = description
            except ValueError as e:
                raise InvalidTaskInputError(f"Invalid description: {str(e)}")

        return True

    def update_task_status(self, task_id: int, completed: bool) -> bool:
        """
        Update the completion status of a task.

        Args:
            task_id (int): The ID of the task to update
            completed (bool): The new completion status

        Returns:
            bool: True if the task status was updated, False if task was not found
        """
        try:
            self._validate_task_exists(task_id)
        except TaskNotFoundError:
            return False

        # Validate completed parameter
        if not isinstance(completed, bool):
            raise InvalidTaskInputError("Completion status must be a boolean")

        # Find and update the task
        for task in self._tasks:
            if task.id == task_id:
                task.completed = completed
                return True

        return False  # This shouldn't happen if validation passed, but included for safety

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if task was not found
        """
        try:
            task = self._validate_task_exists(task_id)
        except TaskNotFoundError:
            return False

        self._tasks.remove(task)
        return True

    @property
    def next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next ID that will be assigned to a new task
        """
        return self._next_id