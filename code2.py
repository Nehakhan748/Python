      #"""PART 4(a)"""

#Simple Grading Program:

#input marks from user:
marks = int(input("Enter marks: "))

#if-else statments
if(marks >= 90 and marks<=100):
        print("Grade is A:")
elif(marks >= 80 and marks <=89):
        print("Grade is B:")
elif(marks >= 70 and marks <=79):
        print("Grade is C:")
elif(marks >= 60 and marks <=69):
        print("Grade is D:")
elif(marks < 60):
        print("Grade is F")
else:
        print("Invalid Marks")

