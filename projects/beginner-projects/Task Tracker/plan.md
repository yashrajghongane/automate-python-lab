# CLI Task Tracker

# v1.0 (Built in Memory version )

# Designed by Yashraj.

---

```Raw Plannning
## what i shoul build -
1. a task tracker cli app that should not crash on bad input
2. it should not be just todo app it has logics , orgnizing , status , filtering
3. This program must be usable tommarow also
```

---

## Plannig

## Datasturcture used in this app -

Dict - storing all the task and their info
list - storing tasks
varible - input/outputs

---

## Features -

```
1. error handling
2. add/update/delete tasks
3. check task completion status
4. have filter option in while showing tasks
```

---

## Design -

```
___ CLI Task Tracker ___

1. Show Tasks
2. Add Task
3. Update task status
4. Update Task
5. Delete Task
6. Exit

Select the option -> 1
Tasks -
1. Show All Tasks -
        Sort by (assending or decending order)
2. Show Completed Tasks
3. Show incompleted Task


Enter the option ->
_____

Select the option -> 2
Enter the Task -> " Task "
Enter the Group of Task -> " Study/Work "
    Task Added.
____

Select the optioin -> 3
1. Show All Tasks -
        Sort by (assending or decending order)
2. Show Completed Tasks
3. Show incompleted Task

    Enter the Task Id No. ->
    Select the Stutus -
    1. completed
    2. incompleted
___

Select the option -> 4
    Shows the tasks as per above
    Select the task_id - update the status
____

Select the option -> 5
    Shows the tasks as per above
    Select the task_id to delete-
        task deleted.
____

Select the option -> 6
    Byee...

```

---

## Current Version Progeress

1. App can Add / update / delete tasks
2. App can sort the task by assending and desendding order by when the added
3. App can update task stutus by task id
4. App can handle bad inputs on many edge cases

## Current Version Bugs (I Found )

1. Whenever i call the show_task() method task upadtes each time and get multiple tasks on "completed_task" : [] and "incompleted_task" : [] of task_db = {}
2. if the task is not avaible in either completed task or incompleted task then also as task id for updating status/task, deleting task
3. maybe have many function calls
4. not fully secured
