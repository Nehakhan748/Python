
def add():                      #Add Function:
     n = input("Enter name: ")
     m = input("Enter marks: ")
     with open("students.txt", "a") as f:
        f.write(f"-> {n}, {m}\n")
        print("Add Student Successfully!")
        
def view():                         #View Function:
    try:   
         with open("students.txt", "r") as f:
             content = f.read()
             if content.strip == " ":
                  print("No student found")
             else:
                  print("-----Student List-----")
                  print(content)
    except FileNotFoundError:
         print("No student found")
         
def delete():                   #Remove Function:
        name = input("Enter student name to delete: ")
        try:
           with open("students.txt", "r") as f:
            lines = f.readlines()
           with open("students.txt", "w") as f:
            # found = False
            for line in lines:
                if line.startswith(name + ","):
                    found = True
                    continue
                f.write(line)
            if found:
              print("Student deleted successfully.")
            else:
                print("Student not found.")
        except FileNotFoundError:
             print("No student records found.")
#using infinite while-loop:
while True:
       #------menu-------
    print("-----Student Management System-----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Remove Student")
    print("4. Exit")
#ask user for choice to perform different task:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        delete()
    elif choice == 4:
       print("Exit!")
       break
    
    else:
       print("Oops! Invalid Choice")
