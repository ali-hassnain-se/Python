"""
Data Structures is a way of organizing, storing, and managing data i computer
so that it can be accessed and modified efficiently.
Types of Data Structures in Python:
List, Tuple, Set, and Dictionary. (these are non-premitive data types)
"""

"""
1. List  - Mutable
List is about collections of different items, it means we can store different
types of data in a single variable like int, string, float. we use brackets []
to declare list
"""

marks=["Tony", 'A', 3.8] # list of marks
print(marks, type(marks))

# length of list
print(len(marks)) # print total number of items

# index
print(marks[0]) # Tony
# in list we can print values from last index and check value in reversed way
# to do this we use marks[-1], it means last index
print(marks[-1]) # 3.8, marks[-2] means 2nd last index 'A'

# slicing a list: it is about taking a part/piece of list -> list_name[start:end]
# in this ending index is not included
print(marks[0:2]) # ['Tony', ''A']
# same thing we can do in reversed order
print(marks[-3:-1]) # ['Tony', ''A']
# if we want to print values until last index we can use this
# print(marks[-3:]) # ['Tony', 'A', 3.8]
# print(marks[0:]) # ['Tony', 'A', 3.8]

"""
here it will print all the list, by default list_name(0:last_index)
print(marks[:]) # ['Tony', 'A', 3.8]
print(marks[:2]) # print from 0 to 1 index -> ['Tony', ''A']

print using for loop
for score in marks:
    print(score)

lists are Mutable, it means they are changeable/modify
if we want to insert value at the end of the list
marks.append(50)
print(marks) # ['Tony', 'A', 3.8, 50]

if we want to insert at specific index
marks.insert(0, 50)
print(marks) # [50, 'Tony', 'A', 3.8, 50]

we can also check if particular value exists in our list or not
print("Tony" in marks) # returns true if exists otherwise false

we can also clear our list
marks.clear()
print(marks, len(marks)) # empty list [] will be print, length will be 0
"""

#---------------------------------------------------------------------------#

"""
2. Tuple - Immutable
it's also like list but in this we can't be change/modify, we use parentheses ()
to declare Tuple, also we can't add parentheses () then it will work also and
it's type will be tuple, we add () to make our code readable
"""
marks2=("Alex", 'B', 2.8, 50, 50)
print(marks2, type(marks2))
# indexed values access
print(marks2[1]) # 'B'

# count the occurence of number
print(marks2.count(50))
# we can print the index of value
print(marks2.index(50)) # 50 comes first time at 3 index
# marks2[0]=100 # it will give error because we can't modify tuple

#---------------------------------------------------------------------------#

"""
3. Set - Cllection of Unique Items
it stores unique values, duplicate values are not allowed in Set, and also it
don't support indexing, we declare it using curly {} brackets
"""

marks3={98, 97, 95, 96, 95, 96}

print(len(marks3), marks3) # 4, it ignore duplicate values, print values in unordered way


#---------------------------------------------------------------------------#

"""
4. Dictionary - (word - meaning) -> {key - value} - Mutable
it is used to store data in the form of key-value pair, by default keys in
dictionary are unique but values can be duplicates
"""

marks4={"Math": 99, "Physics": 97, "Chemistry": 99}
print(marks4, type(marks4))

# we access value in dictionary using key instead of index
# we can modify existing values
marks4["Physics"]=95
print(marks4["Physics"]) # 95 instead of 97

# we can also add new value
marks4["English"]=90 # it will be added at the last
print(marks4["English"])

# print using for loop
for key in marks4:
    print(key, marks4[key])

#---------------------------------------------------------------------------#

"""
NOTE: Mutable data types are generally slower as compared to Immutable data 
types because Immutable data types have no modification/changing or addition
are not allowed that's why these are faster and simpler in memory
"""

#---------------------------------------------------------------------------#

# PRACTICAL EXERCISE 05
"""
Given a list of roll_numbers: [101, 105, 102, 101, 108, 105, 110]. print all
unique roll_numbers in the list.
"""
roll_nums=[101, 105, 102, 101, 108, 105, 110]
# convert all them into set so duplicates will be ignored
unique_roll_nums=set(roll_nums)
# now print unique roll_numbers
print(unique_roll_nums)

"""
Given Employee records in the form of a list of tuples where each tuple 
contains: (Employee_ID, Employee_Name, Salary)
Example: [
           (101, "Alice", 50000),
           (102, "Gray", 65000),
           (103, "Charle", 45000)
        ]
Ask user to Enter Employee_ID and search it inside records.        
"""

emp_record=[
           (101, "Alice", 50000),
           (102, "Gray", 65000),
           (103, "Charlie", 45000)
        ]

# input() always returns a string, so int() converts it to an integer
# to make it comparable with the integer IDs in the records
emp_id=int(input("Enter Employee ID: "))

found=False
for i in emp_record:
    if(emp_id==i[0]):
        print(i)
        found=True
        break
if not found:
    print("Employee Not Found")

"""
Second Way, By using Tuple Unpacking

# Loop over the list; each round takes one tuple out of emp_record.
# Tuple unpacking: the 3 values of the tuple are assigned to eid, name, salary.
# Example for the first round: eid = 101, name = "Alice", salary = 50000
# (the number of names on the left must match the number of items in the tuple,
#  otherwise Python raises a ValueError)
for eid, name, salary in emp_record:
    if emp_id == eid:
    # f-string: the {} placeholders are replaced with the variable values
        print(f"ID: {eid}, Name: {name}, Salary: {salary}")
        break
else:
    print("Employee Not Found")
"""