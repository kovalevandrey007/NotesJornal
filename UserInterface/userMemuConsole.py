import UserInterface.menuTemplates as men


def menu_console():
        men.printNenuTitle("Главное меню\n           NOTES")
        print("1 - вывод журнала заметок \n2 - вывод заметки по id \n3 - выбор заметки по дате\n4 - редактирование заметки"
              " \n5 - добавление заметки\n6 - удаление заметки\n7 - выход")
        men.printMenuLine()
        print("\n введите пункт из меню ")


