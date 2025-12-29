"""
Custom exception classes for the todo application.
"""


class TaskNotFoundError(Exception):
    """
    Raised when a task with a specific ID is not found.
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found.")


class InvalidTaskInputError(Exception):
    """
    Raised when invalid input is provided for a task.
    """
    def __init__(self, message: str):
        super().__init__(message)


class DuplicateTaskError(Exception):
    """
    Raised when attempting to create a task with an ID that already exists.
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} already exists.")