def to_do_list():
    tasks = []

    while True:
        print("\n To-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if tasks:
                print("Your tasks: ")
                for i, task in enumerate(tasks, 1):
                     print(f"{i}. {task}")
            else:
                print("No tasks added")

        elif choice == "2":
            task = input("Enter a task: ").strip()
            tasks.append(task)
            print(f"{task} has been added to the list")

        elif choice == "3":
            task_num=int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"task '{removed_task}' removed.")
            else:
                print("Invalid task number")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Option")
to_do_list()




