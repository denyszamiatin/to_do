from datetime import datetime

tasks = {}

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
    if date in tasks:
        tasks[date].append(description)
    else:
        tasks[date] = [description]

def return_today_tasks():
    today = datetime.today().strftime('%d.%m.%Y');
    if today in tasks:
        return tasks[today]
    else:
        return None


def del_task_by_date(date, index):
    if date in tasks and len(tasks[date]) - 1 >= index:
        tasks[date].pop(index)
