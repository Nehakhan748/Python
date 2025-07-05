
          #"""PART 4(b)"""

#Basic Logic System:

#fixed username and password:
fixed_username = "Neha Khan"
fixed_password = 44506
#ask the user to input username and password:
username = input("Enter username: ")
password = int(input("Enter password: "))
#use if-else statment:
if( username == fixed_username and password == fixed_password):
        print("Logic Successful")
else:
        print("Access Denied")