# Python Console Todo Application

A simple, in-memory todo application that runs in the console. This application allows users to manage tasks with the following operations:
- Add new tasks
- View all tasks
- Update task details
- Delete tasks
- Mark tasks as complete/incomplete

## Features

- Console-based interface
- In-memory storage (no persistence)
- Support for all 5 core operations: Add, View, Update, Delete, Mark Complete/Incomplete
- Each task includes ID, title, description, and completion status
- Robust error handling with user-friendly messages
- Input validation to prevent invalid data
- Clear and consistent user feedback

## Requirements

- Python 3.13 or higher

## Installation

No installation required. Simply run the application with Python.

## Usage

Run the application using:
```bash
python src/cli/main.py
```

Or if installed as a package:
```bash
todo
```

The application will present a menu with options to perform various operations on your todo list.

## Operations

1. **Add Task**: Create a new task with a title and description
   - Enter a unique title for the task (1-200 characters)
   - Optionally provide a description (up to 1000 characters)
   - Task will be created with unique ID and "incomplete" status

2. **View All Tasks**: Display all tasks with their status
   - Shows all tasks with ID, title, description, and completion status
   - Uses clear status indicators: ○ for incomplete, ✓ for complete

3. **Update Task**: Modify the title or description of an existing task
   - Enter the task ID to update
   - Optionally enter new title and/or description
   - Only specified fields will be updated

4. **Delete Task**: Remove a task from the list
   - Enter the task ID to delete
   - Confirmation required before deletion
   - Cannot be undone

5. **Mark Complete/Incomplete**: Update the completion status of a task
   - Enter the task ID to modify
   - Task status will be toggled
   - Confirmation message provided

## Error Handling

The application provides robust error handling:
- Invalid task IDs are caught with clear error messages
- Empty or invalid titles are rejected with helpful feedback
- Non-existent tasks are handled gracefully
- Input validation prevents invalid data entry
- All error messages are user-friendly and informative

## Data Model

Each task contains:
- ID: Unique identifier (auto-generated)
- Title: Brief description of the task (required, 1-200 characters)
- Description: Detailed information about the task (optional, up to 1000 characters)
- Completion Status: Boolean indicating if the task is complete (True) or incomplete (False)