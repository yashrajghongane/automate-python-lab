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
        "task_group": g_task,
        "status": False
    }
    task_db["tasks"].append(new_task)
    print(f"TasK Added with Task id No of {task_id}")


# Function for showing tasks
def show_task():
    if len(task_db["tasks"]) == 0:
        print("No Task Avaible. ")
    else:
        print(end =" ")
        print("\n 1. Show all Tasks. \n 2. Show Completed Tasks. \n 3. Show incompleted Tasks. \n 4. Show by Groups")
        print(end=" ")
        while True:
            try:
                print(end=" ")
                choice = int(input(" Enter the You choice : "))
            except ValueError:
                print("You have Entered Invalid Choice, Try Again! ")
                print()
                continue
            if choice == 1:
                try:
                    print(end="  ")
                    sort_order = int(input(" Select Sort Order \n 1. Assending \n 2. Dessending -> "))
                    if sort_order == 1:
                        sort = True
                    elif sort_order == 2:
                        sort = False
                    else:
                        print("You have Entred wrong option, Try again.")
                        continue
                    if sort != False:
                        print(end=' ')
                        print("All Tasks: ")
                        for task in task_db["tasks"]:
                             print(f" \n Task Id : {task["task_id"]} \n Task : {task["task"]} \n Group : {task["task_group"]} \n Status : {task["status"]}")  

                        break
                    else:
                        reversed_task = task_db["tasks"]
                        reversed_task.reverse()
                        print(end=' ')
                        print("All Tasks: ")
                        for task in reversed_task:
                            print(f" \n Task Id : {task["task_id"]} \n Task : {task["task"]} \n Group : {task["task_group"]} \n Status : {task["status"]}")  
                        break
                except TypeError as err:
                    print("You have Entred wrong option, Try Again.")
                    print(err)
                    break
                print()
            elif choice == 2:
            
                print()
            elif choice == 3:
            
                print()
            elif choice == 4:
            
                print()
            else:
                print("You have Entered Invalid Choice, Try Again! ")
                print()
                continue

    

# While loop for keep app runnig
while True:
    print("1. Show Task. ")
    print("2. Add Task. ")
    print("3. Update Task Status. ")
    print("4. Update Task")
    print("5. Delete Task.")
    print("6. Exit. ")
    print()
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