# Error Handling Documentation

## Overview
This document describes the error handling mechanisms implemented in the Python console todo application to ensure robustness and provide user-friendly error messages.

## Error Types and Handling

### 1. Invalid Input Errors
**Scenario**: User provides invalid input (e.g., non-numeric task ID, empty title)
**Handling**:
- Input validation occurs at both CLI and service levels
- User receives clear error message explaining the issue
- Application continues running (does not crash)

**Examples**:
- Empty task title: "Error: Title cannot be empty or contain only whitespace."
- Non-numeric task ID: "Error: Invalid task ID. Please enter a number."
- Non-existent task ID: "Error: Task with ID {task_id} not found."

### 2. Task Not Found Errors
**Scenario**: User attempts to operate on a task that doesn't exist
**Handling**:
- Application checks for task existence before operations
- Clear error message indicates the specific task ID that was not found
- Operation is gracefully canceled

**Example**: "Error: Task with ID 999 not found."

### 3. Validation Errors
**Scenario**: User provides data that fails validation (e.g., title too long)
**Handling**:
- Validation occurs at the model level with clear error messages
- Invalid operations are prevented
- User is informed of the specific validation rule that was violated

**Examples**:
- Title too long (>200 characters): "Title must not exceed 200 characters"
- Description too long (>1000 characters): "Description must not exceed 1000 characters"

## Exception Classes

### TaskNotFoundError
Raised when a specific task ID cannot be found in the system.

### InvalidTaskInputError
Raised when invalid input is provided for task creation or updates.

## Best Practices Implemented

1. **Early Validation**: Input is validated as early as possible in the process
2. **Clear Messages**: Error messages are user-friendly and explain what went wrong
3. **Graceful Degradation**: The application continues running after errors
4. **Consistent Format**: All error messages follow a consistent format
5. **Dual Validation**: Both CLI and service layers validate inputs for comprehensive protection

## Input Sanitization

All user inputs are sanitized to:
- Remove leading/trailing whitespace
- Prevent empty or whitespace-only values
- Validate numeric inputs before conversion
- Apply length limits to prevent abuse