
class ToDoList:
    '''Список задач с функциями добавления и удаления'''

    menu = {'1': 'Добавить задачу', '2': 'Список задач', '3': 'Выполнить задачу',
            '4': 'Повторить задачу', '5': 'Выйти'}

    def __init__(self):
        self.todo_items = []  # Список задач

    def add_todo(self, items):
        self.todo_items.append(items)

    def list(self):
        print('Список задач:')
        for item in self.todo_items:
            print(str(item.num) + '. ' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()

    def run(self):

        while True:
            print('Меню:')
            for key, value in ToDoList.menu.items():
                print(key + '. ' + value, end='\n')
            print()
            print('Выберите пункт меню:', end=' ')
            command = input()
            if command == '1':
                self.add_todo(ToDoItem(input('Что добавить? ')))
                print()
                print('Новая задача добавлена', end='\n\n')
            elif command == '2':
                self.list()

            elif command == '3':
                key = int(input('Номер выполненной задачи: '))
                for item in self.todo_items:
                    if item.num == key:
                        item.check()
                        print(f'Задача {key} выполнена')
                        break
                else:
                    print(f'Задача {key} не найдена')

            elif command == '4':
                key = int(input('Номер задачи для повторения: '))
                for item in self.todo_items:
                    if item.num == key:
                        item.uncheck()
                        print(f'Задача {key} повторена')
                        break
                else:
                    print(f'Задача {key} не найдена')

            elif command == '5':
                print('Программа завершена.')
                break


class ToDoItem:
    counter = 0

    def __init__(self, new_do):
        self.is_done = False
        ToDoItem.counter += 1
        self.num = ToDoItem.counter
        self.todo = new_do

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False


if __name__ == '__main__':
    todo_1 = ToDoList()
    todo_1.run()
