from main import add_task, fail_if_invalid_date, input_date, input_description

def menu():
    print "This is Todo List. Please input your choice."

    while True:
        print """
        1. Add Task
        2. Exit
        """
        choice = raw_input('Your choice: ')
        if choice == '1':
            add_task(fail_if_invalid_date(input_date()), input_description())
        elif choice == '2':
            exit()
        else:
            print 'Wrong choice try again'
            continue

menu()