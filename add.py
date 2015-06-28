__author__ = 'illes'
from datetime import datetime, date
from create_list1 import task

"""
adding date and text in global value task
"""
def date_validate(my_date):
    try:
        day, month, year = my_date.split('.')
        d = date(int(year), int(month), int(day))
        res = d.strftime('%d.%m.%Y')
        return res
    except ValueError:
        raise Exception('Date was setted with errors')

def add(date, text):
    task.append([date_validate(date), text])
