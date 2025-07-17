        #"""Simple Contact Book"""

#Empty dictionary to store contacts
contact_list = {}
#Functions
def STORE():                                         #Store Function
        name = input("Enter a name: ")
        phone_no = int(input("Enter a phone number: "))
        contact_list[name] = phone_no
        print(f"Contact { name} added.")
def SEARCH():                                        #Search Function
      name = input("Enter a name to search: ")
      if name in contact_list:
            print(f"Name: { name}")
      else:
            print("name is not found.")
def DELETE():                                        #Delete Function
      name = input("Enter a name to remove: ")
      if name in contact_list:
            contact_list.pop(name) 
      else:
            print("Entered name is not found: ")
def VIEW():                                          #View Function
      print("-----Contact List-----")
      if len(contact_list) == 0:
            print("No name in the list.")
      else:
            for name in contact_list:
                print("-> " + name)  


#Infinite While-loop to do multiple task
while True:
    print("-----Simple Contact Book-----")
    print("1. Store Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contact")
    print("5. Exit")

    #Input Choice from user
    choice = input("Enter your choice (1-4): ")
    #if else statement:
    if choice == "1":
         STORE()
    elif choice == "2":
          SEARCH()
    elif choice == "3":
          DELETE()
    elif choice == "4":
          VIEW()
    elif choice == "5":
          #Exit the program
          print("Exit the program!")
          break
    else:
          print("Invalid Choice.")