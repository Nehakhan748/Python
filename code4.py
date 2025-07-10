              #"""Student List Manager Program"""

# Create an empty list to store student names:
student_list = []
#infinite loop for the menu:
while True:
    #Print menu options:
    print("\n====== Student List Manager ======")
    print("1. Add student")            #choice 1 to add student name
    print("2. Remove student")         #Choice 2 to remove any student name
    print("3. View all students")      #Choice 3 to view all student name
    print("4. Exit")                   #Choice 4 to exit the current loop
    #Input Choice from user
    choice = input("Enter your choice (1-4): ")
    #Use if-else statement to perform menu's task:
    if choice == "1":      
        #Input student name(Add Student):
        name = input("Enter student name to add: ")
        student_list.append(name)
        print(name + " has been added to the list.")
    elif choice == "2":
        #Remove any student name(Remove student):
        name = input("Enter student name to remove: ")     #Input name
        if name in student_list:
            student_list.remove(name)
            print(name + " has been removed from the list.")
        else:
            print(name + " is not in the list.")
    elif choice == "3":
        # View all students
        print("\n--- Student List ---")
        if len(student_list) == 0:
            print("No students in the list.")
        else:
            for student in student_list:
                print("-> " + student)         #print student name list from list:
    elif choice == "4":
        #Exit the program:
        print("Exit!")
        break  #Stop the current loop:
    else:
        #Invalid input choice:
        print("Invalid choice. Please enter a number between 1 and 4.")
