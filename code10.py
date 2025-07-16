       #"""Basic Calculator (Function-Based)"""

#Functions:
def SUM(a, b):                        #Sum function:
  print(f"{a} + { b} =", a+b)     
def SUBTRACT(a, b):                   #Subtract function:
  print(f"{a} - { b} =", a-b)
def MULTIPLE(a, b):                   #Multiply function:
  print(f"{a} * { b} =", a*b)
def DIVIDE(a, b):                     #Divide function:
  print(f"{a} / { b} =", a/b)

#while loop 
while True:
    #Input two numbers:
     num1 =float(input("Enter first number: ")  )      #First number input
     num2 = float(input("Enter second number: "))      #Second number input
     #Input an operator:
     op = input("Enter operators(+, -, /, *): ")
     if op == "+":
       SUM(num1, num2)
     elif op == "-":
      SUBTRACT(num1, num2)
     elif op == "*":
      MULTIPLE(num1, num2)
     elif op == "/":
       if num2 != 0:
         DIVIDE(num1, num2 )
       else:
          print("cannot divided by zero.")
     else:
       print("Invalid Operator.")