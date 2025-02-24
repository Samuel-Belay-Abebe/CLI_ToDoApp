"""A todoapp that runs on the command line."""

from modules.lists import Lists
from modules.extensions import check_for_errors, check_quit_protocol, get_numbered_list

class ToDoApp(Lists):
    """A simple CLI representation of a todoapp."""

    def __init__(self):
        """Iniitialze attributes essential for a todoapp."""
        super().__init__()
    
    def show_todo_list(self):
        """Show the to do list."""
        print("\n_ _ _ To Do List _ _ _")

        # Print the tasks in a formatted manner.
        get_numbered_list(self.todolist)
    
    def show_completed_tasks(self):
        """Show the list of completed tasks."""
        print("\n_ _ _ Completed Tasks _ _ _")

        # Print the tasks in a formatted manner.
        get_numbered_list(self.completed_tasks)
    
    def add_task(self):
        """Add a task to the to do list."""

        task = input("Enter the task you want to add: ")
        # Check for 'q' response.
        check_quit_protocol(task)

        self.todolist.append(task)
        print(f"ADDED TASK: {task}")
        
        # End by showing the user the changes that were made.
        self.show_todo_list()

    def edit_task(self):
        """Edit a task at index:task_number in the to do list."""

        # Check for valid input using check_for_errors function. 
        question = "\nEnter the number of the task you want to edit: "
        task_number = check_for_errors(question, self.todolist)

        edit = input("Enter your edit: ")
        # Check for 'q' response.
        check_quit_protocol(edit)
        
        # The task is at index-1 to compensate python's off-by-one behavior.
        self.todolist[task_number - 1] = edit
        print(f"EDITED TO: {edit}")

        # End by showing the user the changes that were made.
        self.show_todo_list()

    def finish_task(self):
        """Move task at index:task_number from to do list to completed tasks."""

        # Check for valid input using check_for_errors function. 
        question = "Enter the number of the task you finished: "
        task_number = check_for_errors(question, self.todolist)

        # The task is at index-1 to compensate python's off-by-one behavior.
        finished_task = self.todolist.pop(task_number - 1)
        self.completed_tasks.append(finished_task)
        print(f"FINISHED TASK: {finished_task}")
        
        # End by showing the user the changes that were made.
        self.show_todo_list()

    def uncheck_task(self):
        """Move a completed task back to our to do list."""

        # Check for valid input using check_for_errors function. 
        question = "Enter the number of the task you want unchecked: "
        task_number = check_for_errors(question, self.completed_tasks)

        # The task is at index-1 to compensate python's off-by-one behavior.
        unchecked_task = self.completed_tasks.pop(task_number - 1)
        self.todolist.append(unchecked_task)
        print(f"UNCHECKED: {unchecked_task}")

    def delete_task(self):
        """Delete task at index:task_number from our to do list."""
        # Check for valid input using check_for_errors function. 
        question = "Enter the number of the task you want deleted: "
        task_number = check_for_errors(question, self.todolist)

        # The task is at index-1 to compensate python's off-by-one behavior.
        print(f"DELETED: {self.todolist[task_number - 1]}")
        del self.todolist[task_number - 1]

        # End by showing the user the changes that were made.
        self.show_todo_list()
    
    def clear_todo_list(self):
        """Delete all tasks in the to do list."""
        self.todolist = []
        print("TO DO LIST HAS BEEN CLEARED")

        # End by showing the user the changes that were made.
        self.show_todo_list()
    
    def clear_completed_tasks(self):
        """Delete all tasks in the completed tasks list."""
        self.completed_tasks = []
        print("COMPLETED TASKS HAS BEEN CLEARED")

        # End by showing the user the changes that were made.
        self.show_completed_tasks()
