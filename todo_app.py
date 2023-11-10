from todo_list import ToDoList


class TodoApp:
    def __init__(self):
        self.todo_lists = []

    def create_list(self, name):
        """Метод для создания нового списка задач"""
        new_todo_list = ToDoList(name)
        self.todo_lists.append(new_todo_list)
        print(f'Создан новый список задач "{name}"')
        print()

    def delete_list(self, index):
        """Метод для удаления списка задач"""
        if index < 0 or index >= len(self.todo_lists):
            print('Список задач не найден.')
            print()
            return False
        deleted_list_name = self.todo_lists[index].name
        del self.todo_lists[index]
        print(f'Список задач {deleted_list_name} удален.')
        print()
        return True

    def edit_list(self, index):
        """Метод для редактирования списка задач"""
        if index < 0 or index >= len(self.todo_lists):
            print('Список задач не найден')
            print()
            return False

        self.todo_lists[index].run()

    def show_lists(self):
        """Метод для вывода списка всех списков задач"""
        if len(self.todo_lists) == 0:
            print('Нет текущих списков задач')
            print()
            return

        print('Список всех списков задач:')
        index = 1
        for todo_list in self.todo_lists:
            print(f'{index}. {todo_list.name}')
            index += 1
        print()

    def main(self):
        """Метод для запуска программы"""
        while True:
            print('Меню:')
            print('1. Создать новый список задач.')
            print('2. Удалить список задач.')
            print('3. Редактировать список задач.')
            print('4. Показать все списки задач.')
            print('5. Выйти.')
            print()

            choice = input('Выберите пункт меню: ')
            print()

            if choice == '1':
                name = input('Введите название списка задач: ')
                self.create_list(name)

            elif choice == '2':
                index = int(input('Введите номер списка задач для удаления: '))
                self.delete_list(index - 1)

            elif choice == '3':
                index = int(input('Введите номер списка задач для редактирования: '))
                self.edit_list(index - 1)

            elif choice == '4':
                self.show_lists()

            elif choice == '5':
                print('Программа завершена.')
                break


if __name__ == '__main__':
    app = TodoApp()
    app.main()
