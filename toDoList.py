class ToDoList:
    """Список задач с функциями добавления и удаления"""

    menu = {
        '1': 'Добавить задачу',
        '2': 'Список задач',
        '3': 'Выполнить задачу',
        '4': 'Повторить задачу',
        '5': 'Удалить задачу',
        '6': 'Выйти'
    }

    def __init__(self, name):
        self.todo_items = []  # Список задач
        self.name = name

    def add_todo(self, item):
        """Добавление новой задачи"""
        if item.todo != "":
            self.todo_items.append(item)
            print(f'Задача {item.num} добавлена')
            print()
        else:
            print("Нельзя добавлять пустую задачу")
            print()
            
    def del_todo(self, key):
        """Удаление задачи по номеру"""
        index = self.find_todo(key)
        if index == -1:
            print(f'Задача {key} не найдена')
            print()
        else:
            del self.todo_items[index]
            print(f'Задача {key} удалена')
            print()

    def list(self):
        print(f'Список задач "{self.name}":')
        for item in self.todo_items:
            print(str(item.num) + '. ' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()

    def find_todo(self, num):
        index = -1
        for item in self.todo_items:
            index += 1
            if item.num == num:
                return index
        return -1

    def run(self):
        while True:
            print('Меню:')
            for key, value in ToDoList.menu.items():
                print(key + '. ' + value, end='\n')
            print()
            print('Выберите пункт меню:', end=' ')
            command = input()
            print()
            if command == '1':
                self.add_todo(ToDoItem(input('Что добавить? ')))
                print()

            elif command == '2':
                self.list()

            elif command == '3':
                key = int(input('Номер выполненной задачи: '))
                index = self.find_todo(key)
                if index != -1:
                    self.todo_items[index].check()
                    print(f'Задача {key} выполнена')
                    print()
                else:
                    print(f'Задача {key} не найдена')
                    print()

            elif command == '4':
                key = int(input('Номер задачи для повторения: '))
                for item in self.todo_items:
                    if item.num == key:
                        item.uncheck()
                        print(f'Задача {key} повторена')
                        print()
                        break
                else:
                    print(f'Задача {key} не найдена')
                    print()

            elif command == '5':
                key = int(input('Номер задачи для удаления: '))
                self.del_todo(key)
            elif command == '6':
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
    name = input('Введите название списка задач: ')

    todo_1 = ToDoList(name)
    todo_1.run()
