from datetime import datetime

from data_create import title_data, body_data, id_data, time_data
import os


def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    title = title_data()
    body = body_data()
    id = id_data()
    time = time_data()
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write(f'№ {id}; ')
        file.write(f'Заголовок: {title}\n {body}\nДата создания заметки: {time}\n\n')


def print_data():
    print('Вывожу данные для Вас\n')
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            line_count = round(len(data) / 4)
            print(*data)

    except FileNotFoundError:
        print("Файл не найден. Создаю пустой файл для работы.")
        with open('data.csv', 'w+', encoding='utf-8') as file:
            data = list(file.readlines())
            line_count = round(len(data) / 4)
            print(*data)
    print(f'Всего {line_count} записей')
    return data


def change_data():
    data = print_data()
    if (len(data) != 0):
        try:
            number_journal = int(input('Введите номер записи, которую Вы хотите изменить: ')) - 1
            result = [''.join(data[i:i + 4]) for i in range(0, len(data), 4)]
            if 0 <= number_journal < len(result):  # Проверка предела записей
                title = title_data()
                body = body_data()
                time = time_data()
                result[number_journal] = (f'№ {number_journal + 1}; Заголовок: {title}\n {body} \n '
                                          f'Дата создания заметки: {time}\n\n')
                data = ''.join(result)
                with open('data.csv', 'w', encoding='utf-8') as file:
                    file.write(data)
            else:
                print('Вы вышли за границы списка, начните заново')
        except ValueError:
            print('\nВы ввели неверное значение\n')
    else:
        print('В файле нет записей. Создайте запись')


def delete_data():
    data = print_data()
    if (len(data) != 0):
        try:
            number_journal = int(input('Введите номер записи, которую Вы хотите удалить:')) - 1
            result = [''.join(data[i:i + 4]) for i in range(0, len(data), 4)]
            if 0 <= number_journal < len(result):  # Проверка предела записей
                result.pop(number_journal)
                for i in range(number_journal, len(result)):
                    result[i] = result[i].replace(f'№ {i + 2}', f'№ {i + 1}')
                    i += 1
                data = ''.join(result)
                with open('data.csv', 'w', encoding='utf-8') as file:
                    file.write(data)
            else:
                print('Вы вышли за границы списка, начните заново')
        except ValueError:
            print('\nВы ввели неверное значение\n')
    else:
        print('В файле нет записей. Создайте запись')


def print_data_by_id():
    data = print_data()
    if (len(data) != 0):
        try:
            number_journal = int(input('Введите номер записи, которую Вы хотите посмотреть:')) - 1
            result = [''.join(data[i:i + 4]) for i in range(0, len(data), 4)]
            if 0 <= number_journal < len(result):
                print(result[number_journal])
            else:
                print('Вы вышли за границы списка, начните заново')
        except ValueError:
            print('\nВы ввели неверное значение\n')
    else:
        print('В файле нет записей. Создайте запись')


def print_data_by_date():
    data = print_data()
    count = 0
    if (len(data) != 0):
        number_journal = input('Введите дату в формате (DD-MM-YYYY), на которую вывести записи:')
        if len(number_journal) == 10:
            result = [''.join(data[i:i + 4]) for i in range(0, len(data), 4)]
            for i in range(len(result)):
                if number_journal in result[i]:
                    print(result[i])
                    count += 1
            if count == 0:
                print('На выбранную Вами дату ничего не найдено')
        else:
            print('Вы ошиблись при вводе даты')

    else:
        print('В файле нет записей. Создайте запись')


