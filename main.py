from datetime import datetime
from collections import defaultdict
from serialize import serialize_tasks, deserialize_tasks

tasks = defaultdict(list)

def input_description():
    return raw_input('Enter task')


def input_date():
    return raw_input('Entere date ("dd.mm.yyyy")')


def read_tasks():
    try:
        global tasks
        tasks = deserialize_tasks()
    except IOError:
        serialize_tasks(tasks)
        return read_tasks()


def fail_if_invalid_date(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return date
    except ValueError:
        raise Exception('Date was setted with errors')


def fail_if_date_not_exists(date):
    if date not in tasks:
        raise Exception('Date not found')


def fail_if_task_not_exists(date, index):
    if not 0 <= index < len(tasks[date]):
        raise Exception('Task not found')


def add_task(date, description):
    tasks[date].append(description)
    serialize_tasks(tasks)


def get_all_tasks(date):
    return tasks.get(date, [])


def read_all_tasks():
    return tasks.copy()


def return_today_tasks():
    today = datetime.today().strftime('%d.%m.%Y');
    return get_all_tasks(today)


def delete_task(date, index):
    fail_if_date_not_exists(date)
    fail_if_task_not_exists(date, index)
    tasks[date].pop(index)


def update_task(date, index, description):
    fail_if_date_not_exists(date)
    fail_if_task_not_exists(date, index)
    tasks[date][index] = description


def print_sorted_tasks():
    date_list = [datetime.strptime(dt, '%d.%m.%Y') for dt in tasks]
    for date in sorted(date_list):
        date = date.strftime('%d.%m.%Y')
        print '\nList of tasks for {}\n'.format(date)
        for i, task in enumerate(sorted(tasks[date])):
            print '\t{} - {}'.format(i, task)
