"""
Range: it is a special function that we use generally in loops, it returns the
sequence from one specific number to another specific number. in this always 
last value will be excluded.(e.g., range(5) -> [0 1 2 3 4], range(n) -> 0 to 
n-1), By Default: range(start=0, stop, step=1)
"""

nums=range(5)

print(nums)  # range(0, 5)

# 1 to 5
range(1, 6) # [1 2 3 4 5]

# WHILE LOOPS
count=1
while count<=5:  # while condition:
    print("Hello World!")
    count+=1

# Triangle Pattern
i=1
while i<=5:
    print(i * "*") # here * is used for concatination, it means "*" will be print i times
    i+=1

# Inverted Triangle
i=5
while i>0:
    print(i * "*")
    i-=1

# FOR LOOPS
# nums=range(5) # 0 to 4

# for i in nums:
#     print(i)

# another method to write this
# for i in range(5):   # 0 to 4
#     print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

# 1 to 10 -> even number print
for i in range(1, 11):
    if i%2==0:
        print("Even: ", i)
    else:
        print("Odd: ", i)

# print above code using range functionalities range(start, stop, step)
for i in range(2, 11, 2):
    print(i)

"""
keywords in python that generally we used with loops that are (break & continue)
break: it is used whenever we want to stop execution of loop
continue:  it is used to skip the iteration
"""

# multiples of 3 [1 to 50] => 21 stop [break]
for i in range(1, 50):
    if(i==21):
        break
    if(i%3==0):
        print(i)

# multiples of 3 [1 to 50] => 21 skip [continue]
for i in range(1, 50):
    if(i==21):
        continue
    if(i%3==0):
        print(i)

# PRACTICAL EXERCISE 04
# print all odd numbers from 1 to 20
for i in range(1, 21, 2):  # range(1, 21)
    print(i)  # if(i%2!=0) print(i)

# print the table of 57
for i in range(1, 11):
    print("57 * ", i, " = ",57*i)

"""
take 2 integers a and b as input, find and print the first number between
1 and 1000 that is divisible by both numbers
"""

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

for i in range(1, 1001):
    if i%a==0 and i%b==0:
        print("First Number Is: ", i)
        break