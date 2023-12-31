import csv

class ToDoList:
    menu = {
        '1': 'Добавить задачу',
        '2': 'Список задач',
        '3': 'Выполнить задачу',
        '4': 'Повторить задачу',
        '5': 'Удалить задачу',
        '6': 'Изменить порядок задач',
        '7': 'Очистить список задач',
        '8': 'Переименовать список',
        '9': 'Сохранить и выйти'
    }

    def __init__(self, name):
        self.todo_items = []
        self.name = name

    def add_task(self, todo: str):
        """Метод для добавления задачи"""
        if todo != "":
            item = ToDoItem(todo)
            self.todo_items.append(item)
            print(f'Задача {item.num} добавлена')
            print()
            return True
        else:
            print("Нельзя добавлять пустую задачу")
            print()
            return False

    def del_task(self, num):
        """Метод для удаления задачи"""
        if len(str(num)) == 0:
            print("Неверный ввод. Пожалуйста, укажите номер задачи.")
            print()
            return False

        if not str(num).isdigit():
            print("Неверный ввод. Пожалуйста, укажите номер задачи числом.")
            print()
            return False

        index = int(num) - 1

        if index < 0 or index >= len(self.todo_items):
            print(f'Задача {num} не найдена')
            print()
            return False

        del self.todo_items[index]
        print(f'Задача {num} удалена')
        print()
        return True

    def clear_all_tasks(self):
        """Метод для очистки всего списка задач"""
        if len(self.todo_items) == 0:
            return False
        self.todo_items = []
        return True

    def rename_list(self, new_name):
        """Метод для переименования списка задач"""
        if self.name == new_name:
            return False
        self.name = new_name
        print(f'Список задач переименован в "{self.name}"')
        print()
        return True

    def list(self):
        """Метод для вывода списка задач"""
        print(f'Список задач "{self.name}":')
        if len(self.todo_items) == 0:
            print('Список задач пуст.')
        else:
            for item in self.todo_items:
                done_mark = "(Выполнено)" if item.is_done else ""
                print(f"{self.todo_items.index(item) + 1}. {item.todo} {done_mark}")
        print()

    def swap_tasks(self, task1, task2):
        """Метод для замены задач местами"""
        index1 = task1 - 1
        index2 = task2 - 1

        if index1 not in range(len(self.todo_items)) or index2 not in range(len(self.todo_items)):
            print("Задача не найдена.")
            return False

        self.todo_items[index1], self.todo_items[index2] = self.todo_items[index2], self.todo_items[index1]
        print(f"Номера задач {task1} и {task2} поменялись местами.")
        print()
        return True

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
                self.add_task(input('Что добавить? '))
                print()

            elif command == '2':
                self.list()

            elif command == '3':
                num = int(input('Номер выполненной задачи: '))
                index = num - 1
                if index in range(len(self.todo_items)):
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
                num = input('Номер задачи для удаления: ')
                self.del_task(num)

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
                self.save_to_csv()
                print(f'Список задач сохранен в файл "{self.name}.csv".')
                break

    def save_to_csv(self):
        """Метод для сохранения списка задач в файл CSV"""
        self.correct_task_number()
        with open(f'{self.name}.csv', 'w', encoding='UTF-8', newline='') as file:
            fieldnames = ['number', 'task', 'is_task_done']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.todo_items:
                writer.writerow(
                    {'number': item.num, 'task': item.todo, 'is_task_done': 'YES' if item.is_done else 'NO'})


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