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

#---------------------------------------------------------------------------#

# INPU#T
# input("Enter Your Name: ") # first method to take input

name=input("Enter Your Name: ") # it will be stored in name variable

# print("Hello", name)
print("Hello " + name) # second way to print "concatination"
# Concatination: when we add two different strings

#---------------------------------------------------------------------------#

"""
COMMENTS 
Sigle Line Comment=[#] & Multi-Line Comments=[""" """]
comments are those part of our code that's ignored by our compiler/interpreter
if we want to inform that what's actually running in our programwe can use them
"""

#---------------------------------------------------------------------------#

# PRACTICE EXCERCISE 01
name="Tony Stark"
age=53
height=1.85

s_name=input("Enter Your Super Hero Name: ")
print(s_name)

#---------------------------------------------------------------------------#

# TYPE CONVERSION/CASTING

age=input("Enter Your Age: ")
print(age, type(age))

"""
here the type of age will be string not int, everything by default that we 
input using input() function is stores as a string irrespective of what type of 
value we are storing there.
"""

# print(age+1) # here it will give error because we can't concatenate INT into STRING
# to fix this thing we do TYPE CASTING/CONVERSION
# we can convert STRING into INT and INT into float, etc, by using functions
# this is how we convert STRING into INT and add 1, now it will not give error
new_age=int(age)+1
print(new_age)
# converting into FLOAT
print(float(new_age))
# we can also convert into BOOLEAN & STRING using bool() & str()
# when we are converting we always see compatiability like we can't convert "abcd"->int alphabets into int

"""
there is two type of CONVERSIONS in Python, one is TYPE CONVERSION & second is
TYPE CASTING

TYPE CASTnIG: it's a type of conversion that is done by programmers/developers.
(e.g., new_age=int(age)+1, print(float(new_age)) explicit(manually)

TYPE CONVERSION: it's a type of conversion that is done by the interpreter
of Python we don't need to tell about it. (e.g., print(1+2.5) output will be
3.5, so it's done by intrepreter of Python) implicit(automatically)
"""

#---------------------------------------------------------------------------#

"""
# SUM Program => a, b => sum

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

sum=a+b
print("Sum Is: ", sum)
"""

#---------------------------------------------------------------------------#

"""
# SUBTRACTION Program => a, b => subtraction

a=int(input("Enter a: "))
b=int(input("Enter b: "))

sub=a-b
print("Subtraction Is: ", sub)
"""

#---------------------------------------------------------------------------#

# STRING Operations

name="Tony Starc" # we can also write like this:- name='Tony Starc'
grade='B' # we can also write it in double quotes("")

# converting whole string into UPPERCASE
print(name.upper())
# converting whole string into lowercase
print(name.lower())

"""
String in python are IMMUTABLE(it means that we can't change a string when 
it's created), when we change in a string it will makes another string but 
in original string we can't modify.
"""
# whenever we apply any operation on strings it doesn't change our original string

# find operation
print(name.find("arc")) # it will return the index if it exists otherwise returns -1
# python follows 0 based indexing

# replace operation

print(name.replace("Tony Starc", "IronMan")) # it will returns a new string IronMan

# check presence operation
print('Z' in name) # prints True if exists otherwise False

#---------------------------------------------------------------------------#

# PRACTICE EXCERCISE 02
apple=99.5
orange=23.75
banana=16.15

sum=apple+orange+banana
totalBill=sum
print(totalBill)
avgBill=sum/3
print(avgBill)

#---------------------------------------------------------------------------#

# ARITHMETIC OPERATORS

"""
Arithmetic operations are symbols used in mathematics and programming to perform
basic calculations.
Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), 
Exponent/Power[used in python](**)

2+2, here + is our operator and 2 is operands
"""

print(5+3) # addition
print(5-3) # subtraction
print(5*3) # multiplication
print(5/3) # division
print(5//3) # if we want to print only integer part and ignore decimal part
print(5%3) # modulus
print(2**3) # exponent/power

# ASSIGNMENT OPERATORS
x=1
x=x+5  # answer will be 6
# x+=5 # we can also write like this 
# x-=1, x/=5, x*=3, x%=5

# OPERATOR PRECEDENCE
"""
it's like BODMAS in math but in programmin we use PRECEDENCE like *,/ has
greater priority than +,-. 2+5*3 (here if we plus first and multiply later all,
all the result will be different) 
"""
ans=2+5*3
print(ans) # answer will be 17 because * has greater priority than +

# COMPARISON OPERATORS
"""
if answer will be true it prints True otherwise False
>, <, <=, >=, ==, !=
"""

print(3>9) # greater tha
print(3<9) # less than
print(3>=9) # greater than or equals to
print(3<=9) # less than or equals to
print(3==9) # equals to
print(3!=9) # not equals to

# LOGICAL OPERATORS
"""
they denotes the logic of our expression, there are three logical operators
(OR, AND, NOT)
"""
st1=3>5
st2=3<5

print(st1 or st2) # prints true if any condition will be true otherwise flase

print((3<5) and (3<12)) # prints True if both conditions true otherwise false

print(not False) # it prints the opposites
print(not (3>2)) # here it's true but due to not operator it prints false