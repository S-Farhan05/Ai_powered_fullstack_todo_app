---
description: "Task list for Python console todo application implementation"
---

# Tasks: Core Todo Functionality

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: No automated tests requested per spec requirements. Only manual testing will be performed.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 [P] Create models directory in src/models/
- [x] T003 [P] Create services directory in src/services/
- [x] T004 [P] Create cli directory in src/cli/
- [x] T005 Create pyproject.toml file with Python 3.13+ configuration
- [x] T006 Create README.md with project documentation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create Task model in src/models/task.py with ID, title, description, and completion status
- [x] T008 Create TodoService in src/services/todo_service.py with in-memory storage
- [x] T009 Create CLI interface structure in src/cli/main.py
- [x] T010 Initialize unique ID counter in TodoService
- [x] T011 Implement basic menu system in main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title, description, and auto-assigned unique ID marked as incomplete

**Independent Test**: Can be fully tested by adding a new task and verifying it appears in the task list with a unique ID and proper status.

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement Task class with required fields in src/models/task.py
- [x] T013 [US1] Implement add_task method in src/services/todo_service.py
- [x] T014 [US1] Implement add task functionality in CLI menu in src/cli/main.py
- [x] T015 [US1] Test adding task with valid inputs and verify unique ID assignment
- [x] T016 [US1] Verify new tasks are created with "incomplete" status by default

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all tasks with their ID, title, description, and completion status

**Independent Test**: Can be fully tested by adding multiple tasks and then viewing them all to confirm they display correctly with status information.

### Implementation for User Story 2

- [x] T017 [P] [US2] Implement get_all_tasks method in src/services/todo_service.py
- [x] T018 [US2] Implement view all tasks functionality in CLI menu in src/cli/main.py
- [x] T019 [US2] Format task display with ID, title, description, and status indicators
- [x] T020 [US2] Test viewing tasks when multiple tasks exist
- [x] T021 [US2] Test viewing tasks when no tasks exist (appropriate message)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P1)

**Goal**: Enable users to update completion status of tasks by specifying task ID

**Independent Test**: Can be fully tested by creating tasks, marking them complete/incomplete, and verifying the status updates correctly.

### Implementation for User Story 5

- [x] T022 [P] [US5] Implement update_task_status method in src/services/todo_service.py
- [x] T023 [US5] Implement mark complete/incomplete functionality in CLI menu in src/cli/main.py
- [x] T024 [US5] Validate task ID exists before updating status
- [x] T025 [US5] Test marking incomplete task as complete
- [x] T026 [US5] Test marking complete task as incomplete

**Checkpoint**: At this point, User Stories 1, 2, and 5 should all work independently

---

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Enable users to modify title or description of existing task by specifying task ID

**Independent Test**: Can be fully tested by creating a task, updating its details, and verifying the changes are reflected when viewing the task.

### Implementation for User Story 3

- [x] T027 [P] [US3] Implement update_task method in src/services/todo_service.py
- [x] T028 [US3] Implement update task functionality in CLI menu in src/cli/main.py
- [x] T029 [US3] Validate task ID exists before updating details
- [x] T030 [US3] Test updating task title and description
- [x] T031 [US3] Verify task ID remains unchanged after update

**Checkpoint**: At this point, User Stories 1, 2, 3, and 5 should all work independently

---

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to remove tasks from their list by specifying task ID

**Independent Test**: Can be fully tested by creating tasks, deleting one, and verifying it no longer appears in the task list.

### Implementation for User Story 4

- [x] T032 [P] [US4] Implement delete_task method in src/services/todo_service.py
- [x] T033 [US4] Implement delete task functionality in CLI menu in src/cli/main.py
- [x] T034 [US4] Validate task ID exists before deletion
- [x] T035 [US4] Test deleting existing task
- [x] T036 [US4] Test attempting to delete non-existent task (appropriate error message)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T037 [P] Add error handling for invalid user inputs across all operations
- [x] T038 [P] Improve CLI user experience with clearer prompts and messages
- [x] T039 Add comprehensive README.md with usage instructions
- [x] T040 Run manual tests following quickstart.md validation
- [x] T041 Verify all functional requirements from spec are met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks can run sequentially as dependencies require
- Once Foundational phase completes, user stories must proceed in priority order due to shared resources
- Models and service methods within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch foundational tasks sequentially:
Task: "Create Task model in src/models/task.py with ID, title, description, and completion status"
Task: "Create TodoService in src/services/todo_service.py with in-memory storage"
Task: "Create CLI interface structure in src/cli/main.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 5 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add tasks)
4. Complete Phase 4: User Story 2 (View tasks)
5. Complete Phase 5: User Story 5 (Mark complete/incomplete)
6. **STOP and VALIDATE**: Test core functionality independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Stories 1, 2, 5 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 → Test independently → Deploy/Demo
4. Add User Story 4 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Sequential Team Strategy

With single developer:

1. Complete Setup + Foundational
2. Once Foundational is done:
   - Complete User Stories 1, 2, 5 (all P1 priority)
   - Complete User Story 3 (P2 priority)
   - Complete User Story 4 (P2 priority)
   - Complete Polish phase

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Focus on manual testing as specified in requirements