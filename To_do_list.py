import os
# To_do_list file
FILE = 'tasks.txt'

# choices
Categories = ['Health', 'Personal', 'Work', 'Financial']
Priority = ['Low', 'Medium', 'High']
Status = ['Pending', 'In_Progress', 'Completed']


def count_lines():
    '''Function to count the no.of lines in a file'''
    if (not os.path.exists(FILE)):
        print('File not Found.')
        return 0
    line_count = 0
    with open(FILE, 'r') as f:
        for i, line in enumerate(f, start= 1):
            line_count += 1
    return line_count


def get_task(prompt):
    '''Function to get text input from user'''
    task = input(prompt).strip()
    while (task == ''):
        print('This should not be empty. Please enter something.')
        task = input(prompt).strip().lower()
    return task


def View():
    '''Function to view the list'''
    if (not os.path.exists(FILE)):
        print('File not found.')
        return
    if (count_lines() == 0):
        print('No tasks avialble to show.')
        return
    with open(FILE, 'r') as f:
        for i,line in enumerate(f, start= 1):
            print(f'{i}. {line.strip()}')


def get_choice(prompt, items_list):
    '''Function to choose from  the givn choices'''
    for i, item in enumerate(items_list, start= 1):
        print(f'{i}. {item}')
    choice = get_number(prompt)
    while (choice not in range(1, len(items_list)+1)):
        print('Invalid choice. Please choose from the above list only.')
        choice = get_number(prompt)
    return items_list[choice - 1]


def Add():
    '''Function to add a new task'''
    if (not os.path.exists(FILE)):
        print('File not found.')
        return
    print('Before adding a new task. The current to do list is: ')
    View()
    task_decription = get_task('Enter task description: ').title()
    print('Task categories are: ')
    task_category = get_choice('Choose from the above categories: ', Categories)
    print('Task priorities are: ')
    task_priority = get_choice('Choose from the above priorities: ', Priority)
    print('Task statuses are: ')
    task_status = get_choice('Choose from the above statuses: ', Status)
    task = f'{task_decription}|{task_category}|{task_priority}|{task_status}'
    with open(FILE, 'a') as f:
        f.write(f'{task}\n')
    print('After adding a new task. The to do list is: ')
    View()


def Edit():
    '''Function to modify an existing task'''
    if (not os.path.exists(FILE)):
        print('File not found.')
        return
    if (count_lines() == 0):
        print('No tasks avialble to modify.')
        return
    print('Before modifying an existing task. The current to do list is: ')
    View()
    line_number= get_number('Enter task no to modify: ')
    while (line_number > count_lines() or line_number < 1):
        print('Entered task number is not in the list. Please enter valid task number.')
        line_number= get_number('Enter task no to modify: ')
    with open(FILE, 'r') as f:
        with open('temp.txt','w') as temp:
            for i, line in enumerate(f, start= 1):
                if (i != line_number):
                    temp.write(f'{line}')
                else:
                    task = line.strip().split('|')
                    task_decription = get_task('Enter new task description or (press "n" to keep old task description only): ')
                    if (task_decription.lower() == 'n'):
                        task_decription = task[0]
                    task_category = get_task('Press anything(except "ENTER") to change the task category or "n" to keep the old category: ').lower()
                    if (task_category == 'n'):
                        task_category = task[1]
                    else:
                        print('Task categories are: ')
                        task_category = get_choice('Choose from the above categories only: ', Categories)
                    task_priority = get_task('Press anything(except "ENTER") to change the task priority or "n" to keep the old priority: ').lower()
                    if (task_priority == 'n'):
                        task_priority = task[2]
                    else:
                        print('Task priorities are: ')
                        task_priority = get_choice('Choose from the above priorities only: ', Priority)
                    task_status = get_task('Press anything(except "ENTER") to change the task status or "n" to keep the old status: ').lower()
                    if (task_status == 'n'):
                        task_status = task[3]
                    else:
                        print('Task statuses are: ')
                        task_status = get_choice('Choose from the above statuses only: ', Status)
    
                    task = f'{task_decription}|{task_category}|{task_priority}|{task_status}'
                    temp.write(f'{task}\n')
    os.replace('temp.txt', FILE)
    print('After modifying an existing task. The to do list is: ')
    View()
                    

def Remove():
    '''Function to remove an existing task from the list'''
    if (not os.path.exists(FILE)):
        print('File not found.')
        return
    if (count_lines() == 0):
        print('No tasks avialble to remove.')
        return
    print('Before removing an existing task. The current to do list is: ')
    View()
    line_number= get_number('Enter task no to remove: ')
    while (line_number > count_lines() or line_number < 1):
        print('Entered task number is not in the list. Please enter valid task number.')
        line_number= get_number('Enter task no to remove: ')
    with open(FILE, 'r') as f:
        with open('temp.txt','w') as temp:
            for i, line in enumerate(f, start= 1):
                if (i != line_number):
                    temp.write(line)
    os.replace('temp.txt', FILE)
    print('After removing an existing task. The to do list is: ')
    View()


def task_operations(choice, tasks):
    '''Function to perfrom the task based on the choice given'''
    while(choice not in tasks):
        print('Invalid choice. Choose from the given tasks above.')
        choice = get_number('Choose a task: ')

    tasks_list = {1: View,
                  2: Add,
                  3: Edit,
                  4: Remove}
    tasks_list[choice]()


def get_number(prompt):
    '''Function to get a proper number from user'''
    while True:
        num = input(prompt).strip()
        try:
            num = int(num)
        except ValueError:
            print('Invalid number. Enter proper numerical value.')
        else:
            return num


def defining_tasks():
    '''Function to show the available tasks'''
    tasks = {1: 'View list',
             2: 'Add a new task',
             3: 'Modify an existing task',
             4: 'Removing an existing task'}
    print('Enter: ')
    for key, value in tasks.items():
        print(f'{key} for {value}')
    return tasks


def main():
    while True:
        tasks = defining_tasks()
        choice = get_number('Choose a task: ')
        task_operations(choice, tasks)
        cont = get_task('Do you want to continue (y/n): ').lower()
        if (cont == 'n'):
            print('Exitting. Have a productive day!!!')
            print('-' * 100)
            break

if (__name__ == '__main__'):
    main()