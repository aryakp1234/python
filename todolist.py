print('To Do List')
tasks=[]
choice='y'
while choice != 'n':
    print("1.add a task")
    print("2.remove task")

    choice=str(input("do you want to continue(1/2/n):"))
    if choice=="n":
      print ("quit")
    if choice=="1":
     task=str(input("enter a task:"))
     tasks.append(task)
     print("task added!")
    elif choice=="2":
     remove_task=str(input("enter the task to remove:"))
     if remove_task in tasks:
      tasks.remove(remove_task)
      print("task removed!")
     else:
       print("task not found!")
print(tasks)
