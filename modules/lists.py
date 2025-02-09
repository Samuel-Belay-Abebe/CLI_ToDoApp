from pathlib import Path
import json

class Lists:
    """Representation of the to do list and completed tasks of our todoapp."""

    def __init__(self):
        """Loads the stored lists from the json files."""

        self.todolist = self.retrieve_list('lists/todolist.json')
        self.completed_tasks = self.retrieve_list('lists/completed_tasks.json')
    
    def save_changes(self):
        """Store the lists to a json file."""
        # Save the to do list.
        todolist = json.dumps(self.todolist)
        Path('lists/todolist.json').write_text(todolist)

        # Save the completed tasks list.
        completed_tasks = json.dumps(self.completed_tasks)
        Path('lists/completed_tasks.json').write_text(completed_tasks)
    
    def retrieve_list(self, file_path):
        """Return list stored at the given file path."""
        path = Path(file_path)
        if path.exists():
            contents = path.read_text()
            stored_list = json.loads(contents)
            return stored_list
        else:
            # If no file at given file path, store and return an empty list.
            list = []
            contents = json.dumps(list)
            path.write_text(contents)
            return list
