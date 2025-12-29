# Data Model: Stability, Structure, and Console Improvements

## Task Entity (Enhanced)

### Fields
- **id** (integer): Unique identifier for the task, auto-generated sequentially
- **title** (string): Brief description of the task, required field with validation
- **description** (string): Detailed information about the task, optional field with validation
- **completed** (boolean): Status indicator showing whether the task is complete (true) or incomplete (false), defaults to false

### Validation Rules (Enhanced)
- ID must be unique within the current session
- Title must not be empty, whitespace-only, or None (with improved validation)
- ID must be a positive integer (with improved validation)
- Completed status must be boolean
- Title and description must not exceed reasonable length limits

### State Transitions
- A task can transition from "incomplete" (completed=False) to "complete" (completed=True)
- A task can transition from "complete" (completed=True) back to "incomplete" (completed=False)
- Once created, title and description can be modified (with validation)
- ID is immutable after creation

## Todo Service (Enhanced)

### Fields
- **tasks** (list): Collection of Task objects stored in memory
- **next_id** (integer): Counter for generating unique IDs for new tasks

### Enhanced Validation Rules
- Each task ID must be unique within the collection
- No duplicate IDs allowed
- The collection is maintained only in memory during application runtime
- All operations validate input parameters before execution

### Methods (with enhanced validation)
- **add_task(title, description)**: Creates a new task with validation for title and description
- **get_all_tasks()**: Returns all tasks without modification
- **get_task_by_id(task_id)**: Retrieves a task by ID with validation
- **update_task(task_id, title, description)**: Updates a task with validation for ID existence and input parameters
- **update_task_status(task_id, completed)**: Updates task status with ID validation
- **delete_task(task_id)**: Deletes a task with ID validation