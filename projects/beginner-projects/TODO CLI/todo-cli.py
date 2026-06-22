# TODO CLI
print("_" * 20,end="")
print(" TODO CLI ",end="")
print("_" * 20,end="\n")
print()

# List for storing all the tasks 
tasks = []

def add_task():
    some_task = input("Type Your Task : ")
    if some_task.strip() == "":
        print("You can not add empty Task. ")
        print()
        return
    tasks.append(some_task)
    print("Task Added.")
    print()

def show_task():
    if len(tasks) == 0:
        print("No task available. ")
        print()
        return
    print("Your Tasks : ")
    for index , task in enumerate(tasks):
        print(end="  ")
        print(f"{index + 1}.{task}")
    print()
        
def delete_task():
    try:
       
        if len(tasks) == 0:
            print("No Task Avaible.")
            print()
            return
        
        show_task()
        index = int(input("Enter the Task No. You want to delete : "))
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
            print("Task Deleted. ")
        else:
            print("You Have Entered Invalid Task No. Try Again! ")
            print()
    except ValueError:
        print("You Have Entered Invalid Task No. Try Again! ")
        print()
    
while True:
    print("1. Add Task. ")
    print("2. View Task. ")
    print("3. Remove Task. ")
    print("4. Exit. ")
    try:
        choice = int(input("Enter the You choice : "))
    except ValueError:
        print("You have Entered Invalid Choice, Try Again! ")
        print()
        continue
    if choice == 1:
        add_task()
    elif choice == 2:
        show_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        break
    else:
        print("You have Entered Invalid Choice, Try Again! ")
        print()
        continue