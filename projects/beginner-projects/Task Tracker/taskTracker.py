# Task Tracker CLI
print("_" * 20,end="")
print(" CLI Task Tracker  ",end="")
print("_" * 20,end="\n")
print()

task_db = {
    "tasks": []
}

# a function that crates taskID on the basis of when they are added
def task_id_gen():
    task_count = len(task_db["tasks"])
    task_count += 1
    # task_id = []
    # task_id.append(task_count)
    # total_Tasks = len(task_id)
    return task_count
    
# add task fun()
def add_task():
    add_task = input("Enter the Task -> ")
    g_task = input("Enter the Group of Task -> ")
    task_id = task_id_gen()
    new_task = {
        "task_id": task_id,
        "task" : add_task,
        "Task_group": g_task
    }
    task_db["tasks"].append(new_task)
    print(f"TasK Added with Task id No of {task_id}")


# Function for showing tasks
def show_task():
    if len(task_db["tasks"]) == 0:
        print("No Task Avaible. ")
    
    print("1. Show all Tasks")

    for task in task_db["tasks"]:
        print(task)

# While loop for keep app runnig
while True:
    print("1. Show Task. ")
    print("2. Add Task. ")
    print("3. Update Task Status. ")
    print("4. Update Task")
    print("5. Delete Task.")
    print("6. Exit. ")
    try:
        choice = int(input("Enter the You choice : "))
    except ValueError:
        print("You have Entered Invalid Choice, Try Again! ")
        print()
        continue
    if choice == 1:
        show_task()
        print()
    elif choice == 2:
        add_task()
        print()
    # elif choice == 3:
    #     update_task_status()
    # elif choice == 4:
    #     update_task()
    # elif choice == 5:
    #     del_task()
    elif choice == 6:
        break
    else:
        print("You have Entered Invalid Choice, Try Again! ")
        print()
        continue