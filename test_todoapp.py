import pytest
from unittest.mock import patch

from modules.todoapp import ToDoApp

@pytest.fixture
def todoapp():
    app = ToDoApp()
    app.todolist = ['1', '2', '3']
    app.completed_tasks = ['one']
    return app

def test_add_task_to_todolist(todoapp):
    """Unit test to ensure adding tasks to our to-do-app works correctly."""
    initial_length = len(todoapp.todolist)

    # Mock input to simulate user entering "Go to the gym"
    with patch('builtins.input', return_value="Go to the gym"):
        todoapp.add_task()  # Calls add_task() with mocked input

    # Check if the task was added
    assert len(todoapp.todolist) == initial_length + 1
    assert "Go to the gym" in todoapp.todolist

def test_edit_task_in_todolist(todoapp):
    """Unit test to ensure editing tasks in our to-do-app works correctly."""

    # Use patch to mock the input function for two user inputs
    with patch('builtins.input', side_effect=['1', 'one']):
        todoapp.edit_task()

    # Check if the task was edited from '1' to 'one'.
    assert todoapp.todolist[0] == 'one'

def test_finish_task_in_todolist(todoapp):
    """Unit test to ensure completing tasks in our to-do-app works correctly."""

    initial_length = len(todoapp.todolist)
    finished_task = todoapp.todolist[0]

    # Mock input to simulate user entering "1" (which becomes 0 internally).
    with patch('builtins.input', return_value="1"):
        todoapp.finish_task()  # Calls add_task() with mocked input
    
    assert len(todoapp.todolist) == initial_length - 1
    assert finished_task in todoapp.completed_tasks

def test_uncheck_task_in_todolist(todoapp):
    """Unit test to ensure unchecking tasks in our to-do-app works correctly."""

    initial_length = len(todoapp.completed_tasks)
    unchecked_task = todoapp.completed_tasks[0]

    with patch('builtins.input', return_value="1"):
        todoapp.uncheck_task() # Calls uncheck_task() with mocked input

    assert unchecked_task in todoapp.todolist
    assert len(todoapp.completed_tasks) == initial_length - 1

def test_delete_task_in_todolist(todoapp):
    """Unit test to ensure deleting tasks in our to-do-app works correctly."""

    initial_length = len(todoapp.todolist)
    deleted_task = todoapp.todolist[0]

    with patch('builtins.input', return_value="1"):
        todoapp.delete_task() # Calls delete_task() with mocked input

    assert deleted_task not in todoapp.todolist
    assert len(todoapp.todolist) == initial_length - 1
    
