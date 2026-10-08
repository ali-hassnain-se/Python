"""
Range: it is a special function that we use generally in loops, it returns the
sequence from one specific number to another specific number. in this always 
last value will be excluded.(e.g., range(5) -> [0 1 2 3 4], range(n) -> 0 to 
n-1), By Default: range(start=0, stop, step=1)
"""

nums=range(5)

print(nums)

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
nums=range(5) # 0 to 4

for i in nums:
    print(i)