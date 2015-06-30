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


def all_tasks_on_date(date):
    if date in tasks:
        return tasks[date]
    else:
        return None 


def return_today_tasks():
    today = datetime.today().strftime('%d.%m.%Y');
    return all_tasks_on_date(today)    


def del_task_by_date(date, index):
    if date in tasks and len(tasks[date]) - 1 >= index:
        tasks[date].pop(index)


def modify_task_by_date_and_index(date, index, description):
    if date in tasks and len(tasks[date]) - 1 >= index:
        tasks[date][index] = description
