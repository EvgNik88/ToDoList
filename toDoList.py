class ToDoList:

    menu = {
        '1': 'Добавить задачу',
        '2': 'Список задач',
        '3': 'Выполнить задачу',
        '4': 'Повторить задачу',
        '5': 'Удалить задачу',
        '6': 'Изменить порядок задач',
        '7': 'Очистка списка задач',
        '8': 'Переименовать список',
        '9': 'Выйти'
    }

    def __init__(self, name):
        self.todo_items = []
        self.name = name

    def add_todo(self, todo: str):
        """Метод для добавления задачи"""
        if todo != "":
            item = ToDoItem(todo)
            self.todo_items.append(item)
            print(f'Задача {item.num} добавлена')
            print()
        else:
            print("Нельзя добавлять пустую задачу")
            print()

    def del_todo(self, num):
        """Метод для удаления задачи"""
        index = self.find_todo(num)
        if index == -1:
            print(f'Задача {num} не найдена')
            print()
        else:
            del self.todo_items[index]
            print(f'Задача {num} удалена')
            self.correct_task_number()
            print()

    def clear_all_tasks(self):
        """Метод для очистки всего списка задач"""
        self.todo_items = []

    def rename_list(self, new_name):
        """Метод для переименования списка задач"""
        self.name = new_name
        print(f'Список задач переименован в "{self.name}"')
        print()

    def list(self):
        """Метод для вывода списка задач"""
        print(f'Список задач "{self.name}":')
        if len(self.todo_items) == 0:
            print('Список задач пуст.')
        else:
            for item in self.todo_items:
                print(str(item.num) + '. ' + item.todo + (' (Выполнено)' if item.is_done else ''))
        print()

    def find_todo(self, num):
        """Метод для поиска задачи по номеру в списке"""
        index = -1
        for item in self.todo_items:
            index += 1
            if item.num == num:
                return index
        return -1

    def swap_tasks(self, task1, task2):
        """Метод для замены задач местами"""
        index1 = self.find_todo(task1)
        index2 = self.find_todo(task2)

        if index1 == -1 or index2 == -1:
            print("Задача не найдена.")
            return

        self.todo_items[index1], self.todo_items[index2] = self.todo_items[index2], self.todo_items[index1]
        self.correct_task_number()
        print(f"Номера задач {index1 + 1} и {index2 + 1} поменялись местами.")
        print()

    def correct_task_number(self):
        """Метод для корректировки номеров задач после изменения порядка"""
        for i in range(len(self.todo_items)):
            self.todo_items[i].num = i + 1

    def run(self):
        """Метод для запуска"""
        while True:
            print('Меню:')
            for key, value in ToDoList.menu.items():
                print(key + '. ' + value)
            print()
            print('Выберите пункт меню:', end=' ')
            command = input()
            print()
            if command == '1':
                self.add_todo(input('Что добавить? '))
                print()

            elif command == '2':
                self.list()

            elif command == '3':
                num = int(input('Номер выполненной задачи: '))
                index = self.find_todo(num)
                if index != -1:
                    self.todo_items[index].check()
                    print(f'Задача {num} выполнена.')
                    print()
                else:
                    print(f'Задача {num} не найдена.')
                    print()

            elif command == '4':
                num = int(input('Номер задачи для повторения: '))
                for item in self.todo_items:
                    if item.num == num:
                        item.uncheck()
                        print(f'Задача {num} повторена.')
                        print()
                        break
                else:
                    print(f'Задача {num} не найдена.')
                    print()

            elif command == '5':
                num = int(input('Номер задачи для удаления: '))
                self.del_todo(num)

            elif command == '6':
                task1 = int(input('Введите номер первой задачи для обмена: '))
                task2 = int(input('Введите номер второй задачи для обмена: '))
                self.swap_tasks(task1, task2)

            elif command == '7':
                print('Список задач очищен.')
                self.clear_all_tasks()
                print()

                choice = input('Хотите переименовать список? (да/нет): ')
                if choice == 'да':
                    new_name = input('Введите новое название списка задач: ')
                    self.rename_list(new_name)
                print()


            elif command == '8':
                new_name = input('Введите новое название списка: ')
                self.rename_list(new_name)


            elif command == '9':
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
