"""
Task model representing a single todo item with ID, title, description, and completion status.
"""

from typing import Optional


class Task:
    """
    Represents a single todo item with ID, title, description, and completion status.
    """

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Brief description of the task (required)
            description (str): Detailed information about the task (optional)
            completed (bool): Status indicator showing whether the task is complete (optional, defaults to False)
        """
        self._validate_task_id(task_id)
        self._validate_title(title)
        self._validate_description(description)
        self._validate_completed(completed)

        self._id = task_id
        self._title = title
        self._description = description
        self._completed = completed

    def _validate_task_id(self, task_id: int) -> None:
        """Validate the task ID."""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

    def _validate_title(self, title: str) -> None:
        """Validate the task title."""
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if title.strip() == "":
            raise ValueError("Title cannot be whitespace-only")
        if len(title) > 200:  # Reasonable length limit
            raise ValueError("Title must not exceed 200 characters")

    def _validate_description(self, description: str) -> None:
        """Validate the task description."""
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if len(description) > 1000:  # Reasonable length limit
            raise ValueError("Description must not exceed 1000 characters")

    def _validate_completed(self, completed: bool) -> None:
        """Validate the completion status."""
        if not isinstance(completed, bool):
            raise ValueError("Completed status must be a boolean")

    @property
    def id(self) -> int:
        """Get the task ID."""
        return self._id

    @property
    def title(self) -> str:
        """Get the task title."""
        return self._title

    @title.setter
    def title(self, value: str):
        """Set the task title."""
        self._validate_title(value)
        self._title = value

    @property
    def description(self) -> str:
        """Get the task description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the task description."""
        self._validate_description(value)
        self._description = value

    @property
    def completed(self) -> bool:
        """Get the task completion status."""
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        """Set the task completion status."""
        self._validate_completed(value)
        self._completed = value

    def __str__(self) -> str:
        """Return string representation of the task."""
        status = "✓" if self.completed else "○"
        return f"[{status}] ID: {self.id} | Title: {self.title} | Description: {self.description}"

    def to_dict(self) -> dict:
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Task instance from a dictionary."""
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )