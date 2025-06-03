# To do list CLI app

todo_list = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
    elif choice == '2':
        print("Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
        else:
            print("Invalid task number.")
    elif choice == '4':
        break
    else:
        print("Invalid option.")
