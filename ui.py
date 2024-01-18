from script import input_data, print_data, delete_data, change_data, print_data_by_id, print_data_by_date


def interface():
    exit = 0
    while (exit != 6):
        print('Добро пожаловать в заметки! Что Вы желаете выполнить?\n'
              '1. Создать новую заметку\n'
              '2. Изменить заметку\n'
              '3. Удалить заметку\n'
              '4. Показать все заметки\n'
              '5. Показать определенную заметку\n'
              '6. Выйти из программы\n')
        try:
            command = int(input('Введите номер операции: '))

            while command < 1 or command > 6:
                print('Попробуйте ещё раз выбрать правильную команду')
                command = int(input('Введите номер операции: '))

            if command == 1:
                input_data()
            elif command == 2:
                change_data()
            elif command == 3:
                delete_data()
            elif command == 4:
                print_data()
            elif command == 5:
                print('По каким параметрам Вам показать запись??\n'
                      '1. По номеру записи\n'
                      '2. Все записи на выбранную дату\n')
                try:
                    command = int(input('Введите номер операции: '))
                    while command < 1 or command > 2:
                        print('Попробуйте ещё раз выбрать правильную команду')
                        command = int(input('Введите номер операции: '))
                    if command == 1:
                        print_data_by_id()
                    elif command == 2:
                        print_data_by_date()
                except ValueError:
                    print('\nВы ввели неверное значение\n')
            elif command == 6:
                exit = 6
        except ValueError:
            print('Вы ввели неверное значение')
