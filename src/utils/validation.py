"""
Input validation utilities for the todo application.
"""


def validate_task_title(title: str) -> bool:
    """
    Validate a task title.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not title or not isinstance(title, str):
        return False
    if title.strip() == "":
        return False
    if len(title) > 200:  # Reasonable length limit
        return False
    return True


def validate_task_description(description: str) -> bool:
    """
    Validate a task description.

    Args:
        description (str): The description to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(description, str):
        return False
    if len(description) > 1000:  # Reasonable length limit
        return False
    return True


def validate_task_id(task_id: int) -> bool:
    """
    Validate a task ID.

    Args:
        task_id (int): The ID to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(task_id, int) or task_id <= 0:
        return False
    return True


def validate_task_completed(completed: bool) -> bool:
    """
    Validate a task completion status.

    Args:
        completed (bool): The completion status to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(completed, bool):
        return False
    return True


def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input by removing leading/trailing whitespace.

    Args:
        input_str (str): The input to sanitize

    Returns:
        str: Sanitized input string
    """
    if input_str is None:
        return ""
    if not isinstance(input_str, str):
        return str(input_str).strip()
    return input_str.strip()


def is_empty_or_whitespace_only(text: str) -> bool:
    """
    Check if text is empty or contains only whitespace.

    Args:
        text (str): The text to check

    Returns:
        bool: True if empty or whitespace-only, False otherwise
    """
    if not text or not isinstance(text, str):
        return True
    return text.strip() == ""


def validate_numeric_input(input_str: str) -> bool:
    """
    Validate if input string can be converted to a number.

    Args:
        input_str (str): The input to validate

    Returns:
        bool: True if numeric, False otherwise
    """
    if not input_str or not isinstance(input_str, str):
        return False
    try:
        int(input_str)
        return True
    except ValueError:
        return False