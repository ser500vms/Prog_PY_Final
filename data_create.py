import datetime as dt


def title_data():
    title = input('Введите заголовок: ')
    return title


def body_data():
    body = input('Введите заметку: ')
    return body


def id_data():
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            id = round(len(data) / 4) + 1
    except FileNotFoundError:
        with open('data.csv', 'w+', encoding='utf-8') as file:
            data = list(file.readlines())
            id = round(len(data) / 4) + 1
    return id


def time_data():
    now = dt.datetime.now(dt.timezone.utc).astimezone()
    time_format = "%d-%m-%Y %H:%M:%S"
    return f'{now:{time_format}}'
