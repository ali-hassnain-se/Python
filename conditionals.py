# Conditional Statements 
"""
conditional statements are the statements in programming that allow a program 
to make decision based on whether a condition is true or false.
"""

age=17

# Indentation: it is used to arrange code by giving proper spacing, all the code
# in python will be executed when we give proper spacing/indentation
if age>=18:
    print("You're An Adult")
    print("You Can Drive / Vote")
elif age<18:
    print("You Can't Drive / Vote")


marks=int(input("Enter Your Marks: "))

if marks >= 80:
    print("A Grade")

elif marks >= 60 and marks <= 79:
    print("B Grade")

else:
    print("C Grade")
