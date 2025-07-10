         #"""Simple To-Do List Manager"""

# Create an empty list to store tasks
tasks = []
#Infinite loop for the task:
while True:
    #Print task options:
    print("\n====== To-Do List Manager ======")
    print("1. Add task")           #Choice 1 to add task
    print("2. Delete task")        #Choice 2 to delete any task
    print("3. View tasks")         #Choice 3 to view all task
    print("4. Exit")               #Choice 4 to exit the current loop
    #Input choice from user:
    choice = input("Enter your choice (1-4): ")
    #Use if-else statement to perform any task by choice:
    if choice == "1":
        #Input task(add task):
        task = input("Enter a task to add: ")
        tasks.append(task)  
        print("Task added: " + task)
    elif choice == "2":
        #Remove any task(Delete Task):
        task = input("Enter the task to delete: ")      #Input task
        if task in tasks:
            tasks.remove(task)
            print("Task removed: " + task)
        else:
            print("Task not found: " + task)
    elif choice == "3":
        #View all task:
        print("\n--- To-Do List ---")
        if len(tasks) == 0:
            print("No tasks in your list.")
        else:
            #Print all tasks
            for item in tasks:
                print("-> " + item)
    elif choice == "4":
        #Exit the program:
        print("Exit!")
        break  #Stop the crrent loop:
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
