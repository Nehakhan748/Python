

# calculator
# 2 digits
# + , -, *, /
# python(console based)

# 2 variables

num1 = float(input("Enter first number: "))
print(type(num1))
op = input("Enter operation(+, -, *, /): ")
num2 = float(input("Enter second number: "))
print(type(num2))

if op == "+":
   result = num1 + num2

elif op == "-":
   result = num1 - num2

elif op == "*":
   result = num1 * num2
elif op == "/":
  if num2 != 0:
     result = num1 / num2
  else:
     print("Cannot divide by zero")

else:
   print("Invalid")

print(f"Result: {result}")
print("Hello!")


