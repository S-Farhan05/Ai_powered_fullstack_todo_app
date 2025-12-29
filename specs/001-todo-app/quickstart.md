# Quickstart Guide: Python Console Todo Application

## Prerequisites
- Python 3.13+ installed on your system
- Basic command-line familiarity

## Setup
1. Clone or create the project directory
2. Ensure Python 3.13+ is available in your environment
3. Navigate to the project directory

## Running the Application
1. Navigate to the project root directory
2. Execute: `python src/cli/main.py`
3. The application will display a menu with available options

## Available Operations
1. **Add Task**: Creates a new task with a unique ID and "incomplete" status
2. **View All Tasks**: Displays all tasks with their ID, title, description, and completion status
3. **Update Task**: Modifies the title or description of an existing task
4. **Delete Task**: Removes a task from the list
5. **Mark Complete/Incomplete**: Updates the completion status of a task

## Usage Example
1. Run the application
2. Select option 1 to add a task, enter title and description
3. Select option 2 to view all tasks
4. Select option 5 to mark a task as complete (enter the task ID)
5. Select option 2 again to verify the status change

## Notes
- All data is stored in memory only and will be lost when the application exits
- Task IDs are automatically generated and sequential
- The application provides console-based interaction only