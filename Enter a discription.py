__author__ = 'viktoria'

def task_description(description):
    task.append([description])
    print task

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
