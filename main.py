from datetime import datetime

tasks = []

def input_description():
    return raw_input('Enter task')


def input_date():
    return raw_input('Entere date ("dd.mm.yyyy")')


def fail_if_invalid_date(my_date):
    try:
        datetime.strptime(my_date, '%d.%m.%Y')
    except ValueError:
        raise Exception('Date was setted with errors')


def add_task(date, description):
    tasks.append([date, description])
