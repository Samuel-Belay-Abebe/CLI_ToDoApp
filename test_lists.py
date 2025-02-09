import json
from pathlib import Path
from unittest.mock import patch

from modules.lists import Lists

def test_save_changes_in_json_files():
    lists = Lists()
    lists.todolist = ['1', '2', '3']
    lists.completed_tasks = ['one']

    # Patch 'write_text' method of 'Path' to prevent actual file writing.
    with patch.object(Path, "write_text") as mock_write_text:
        lists.save_changes()

        # Assert: Ensure 'write_text' was called with correct JSON data.
        mock_write_text.assert_any_call(json.dumps(lists.todolist))
        mock_write_text.assert_any_call(json.dumps(lists.completed_tasks))

def test_retrieve_list_from_json_files():
    lists = Lists()

    file_pathes = ['lists/todolist.json', 'lists/completed_tasks.json']
    for file_path in file_pathes:
        if Path(file_path).exists():
            # Get list stored in json file for later comparison.
            contents = Path(file_path).read_text()
            stored_list = json.loads(contents)

            retrieved_list = lists.retrieve_list(file_path)

            # Assert that list retrieved is same as list in the json file.
            assert retrieved_list == stored_list

def test_retrieve_list_from_empty_json_file():
    lists = Lists()

    file_path = ''
    if not Path(file_path).exists():
        with patch.object(Path, "write_text") as mock_write_text:
            retrieved_list = lists.retrieve_list(file_path)

            mock_write_text.assert_any_call(json.dumps([]))

            # Assert that the returned list will be empty.
            assert not retrieved_list
            