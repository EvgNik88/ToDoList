import pytest

from todo_list import ToDoList, ToDoItem





def test_add_todo(print_test_list, create_test_list):
    test_list = create_test_list
    assert len(test_list.todo_items) == 0
    assert test_list.add_task('Task 1')
    assert len(test_list.todo_items) == 1
    assert test_list.add_task('Task 2')
    assert test_list.todo_items[-1].todo == 'Task 2'
    assert not test_list.add_task("")
    assert len(test_list.todo_items) == 2


def test_del_todo(create_test_list, print_test_list):
    test_list = create_test_list
    test_list.add_task('Task 1')
    test_list.add_task('Task 2')
    test_list.add_task('Task 3')
    temp = test_list.todo_items[2].num
    assert test_list.del_task(3)
    temp2 = [i for i in test_list.todo_items if i.num == temp]
    assert len(temp2) == 0
    assert not test_list.del_task(9)
    assert not test_list.del_task('a')


def test_clear_all_tasks(create_test_list, print_test_list):
    test_list = create_test_list
    assert not test_list.clear_all_tasks()
    test_list.add_task('Task 1')
    test_list.add_task('Task 2')
    test_list.add_task('Task 3')
    assert test_list.clear_all_tasks()
    assert len(test_list.todo_items) == 0


def test_rename_list(create_test_list, print_test_list):
    test_list = create_test_list
    assert not test_list.rename_list('Test')
    test_list.rename_list('BlaBla')
    assert test_list.name == 'BlaBla'


def test_swap_tasks(create_test_list, print_test_list):
    test_list = create_test_list
    test_list.add_task('Task 1')
    test_list.add_task('Task 2')
    test_list.add_task('Task 3')
    test_list.add_task('Task 4')
    test_list.swap_tasks(1, 4)
    assert test_list.todo_items[0].todo == 'Task 4'
    assert test_list.todo_items[3].todo == 'Task 1'
    assert not test_list.swap_tasks(1, 8)


