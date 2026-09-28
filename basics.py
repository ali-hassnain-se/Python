# OUTPUT
# print("Hello", "World!")
# # Here if we use comma(,) it will seperate strings otherwise print them combines

""" 
VARIABLES
Variable: variable is a named storage location that is used to store value
"""
# name="Rana Ali Hassnain" # string
# age=19 # integer
# cgpa=3.9 # float
# is_Student=True # boolean
# print(name, age, cgpa, is_Student)

# # print data type of variables
# print(type(name))

# INPU#T
# input("Enter Your Name: ") # first method to take input

name=input("Enter Your Name: ") # it will be stored in name variable

# print("Hello", name)
print("Hello " + name) # second way to print "concatination"
# Concatination: when we add two different strings

"""
COMMENTS 
Sigle Line Comment=[#] & Multi-Line Comments=[""" """]
comments are those part of our code that's ignored by our compiler/interpreter
if we want to inform that what's actually running in our programwe can use them
"""

# PRACTICE EXCERCISE 01
name="Tony Stark"
age=53
height=1.85

s_name=input("Enter Your Super Hero Name: ")
print(s_name)

# TYPE CONVERSION/CASTING

age=input("Enter Your Age: ")
print(age, type(age))

"""
here the type of age will be string not int, everything by default that we 
input using input function it stores as a string irrespective of what type of 
value we are storing there
"""

# print(age+1) # here it will give error because we can't concatenate INT into STRING
# to fix this thing we do TYPE CASTING/CONVERSION
# we can conver STRING into INT and INT into float, etc, by using functions
# this is how we convert STRING into INT and add 1, now it will not give error
new_age=int(age)+1
print(new_age)
# converting into FLOAT
print(float(new_age))
# we can also convert into BOOLEAN & STRING using bool() & str()
# when we are converting we always see compatiability like we can't convert "abcd"->int alphabets into int

"""
there is two type of CONVERSIONS in Python, one is TYPE CONVERSION & TYPE 
CASTING

TYPE CASTIG: it's a type of conversion that is done by programmers/developers.
(e.g., new_age=int(age)+1, print(float(new_age))) explicit(manually)

TYPE CONVERSION: it's a type of conversion that is done by the interpreter
of Python we don't need to tell about it. (e.g., print(1+2.5) output will be
3.5, so it's done by intrepreter of Python) implicit(automatically)
"""