        #"""Basic Calculator with While Loop"""

#while loop 
while True:
    #Input two numbers:
     num1 =input("Enter first number: ")        #First number input
     if num1 == "exit":       #If exit the loop:
       print("Exit!")
       break
     num2 = input("Enter second number: ")      #Second number input
     #Input an operator:
     op = input("Enter operators(+, -, /, *): ")
     # Convert input numbers from strings to floats
     numb1 = float(num1)
     numb2 = float(num2)
     if op == "+":
      result = numb1 + numb2 
     elif op == "-":
      result = numb1 - numb2 
     elif op == "*":
       result = numb1 * numb2 
     elif op == "/":
       if numb2 != 0:
         result = numb1 / numb2 
       else:
          print("cannot divided by zero.")
     else:
       print("Invalid Operator.")
     print(f"Result:", result)