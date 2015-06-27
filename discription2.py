__author__ = 'viktoria'

name = _import_('create_list1')

def task_description(description):
    name.task.append([description])
    print name.task

while True:
    print 'If you want enter new task press - a'
    print 'If you want quite press - q'

    s = raw_input('what you want? ')
    if s == 'q':
        break
    elif s == 'a':
        description = str(raw_input('Enter task'))
        task_description(description)
    else:
        exit()
