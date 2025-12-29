# Data Model: Core Todo Functionality

## Task Entity

### Fields
- **id** (integer): Unique identifier for the task, auto-generated sequentially
- **title** (string): Brief description of the task, required field
- **description** (string): Detailed information about the task, optional field
- **completed** (boolean): Status indicator showing whether the task is complete (true) or incomplete (false), defaults to false

### Relationships
- The Task entity exists independently with no required relationships to other entities

### Validation Rules
- ID must be unique within the current session
- Title must not be empty or None
- ID must be a positive integer
- Completed status must be boolean

### State Transitions
- A task can transition from "incomplete" (completed=False) to "complete" (completed=True)
- A task can transition from "complete" (completed=True) back to "incomplete" (completed=False)
- Once created, title and description can be modified
- ID is immutable after creation

## Todo List Collection

### Fields
- **tasks** (list): Collection of Task objects stored in memory
- **next_id** (integer): Counter for generating unique IDs for new tasks

### Relationships
- Contains multiple Task entities
- Manages the lifecycle of Task entities (create, update, delete, mark complete/incomplete)

### Validation Rules
- Each task ID must be unique within the collection
- No duplicate IDs allowed
- The collection is maintained only in memory during application runtime