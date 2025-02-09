from modules.todoapp import ToDoApp
from modules.extensions import show_commands

# Start by instantiating our to do application.
todoapp = ToDoApp()

# Start by setting instructions for our program.
instructions = "ENTER 'q' TO QUIT AT ANYTIME!"
instructions += "\nENTER 'show_commands' TO SHOW COMMANDS YOU CAN USE."
print(instructions)

# Store all names of available commands and their functions as values.
commands = {
    # Remove the parentheses to stop python from running them upon definition.
    "show_todo_list": todoapp.show_todo_list, 
    "show_completed_tasks": todoapp.show_completed_tasks, 
    "add_task": todoapp.add_task, 
    "edit_task": todoapp.edit_task,
    "finish_task": todoapp.finish_task, 
    "uncheck_task": todoapp.uncheck_task, 
    "delete_task": todoapp.delete_task,
    "clear_todo_list": todoapp.clear_todo_list,
    "clear_completed_tasks": todoapp.clear_completed_tasks
    }

# Show the to do list and list of completed tasks.
todoapp.show_todo_list()
todoapp.show_completed_tasks()

while True:
    selected_command = input("\nEnter command: ")
    if selected_command in commands:
        for command in commands:
            if selected_command == command:
                # Add parentheses to properly call the functions.
                commands[command]()
                # End with saving changes to the json files.
                todoapp.save_changes()
    elif selected_command == 'q':
        # If the user inputs 'q' exit the program.
        break
    elif selected_command == 'show_commands':
        show_commands(commands)
    else:
        # If the user enters any other command, print out an error.
        print("INPUT A VALID COMMAND!")
