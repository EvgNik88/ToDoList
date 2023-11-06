import pytest
from todo_list import ToDoList

test_list = ToDoList('Test')

@pytest.fixture
def create_test_list():
    test_list.clear_all_tasks()
    return test_list

@pytest.fixture
def print_test_list():
    yield
    test_list.list()

