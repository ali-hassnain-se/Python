# Functions
"""
A function is a block of code that performs a specific task and can be reused 
whenever needed. it reduce redundancy (writing the same code repeatedly).
1. User-Define Functions (sum(), sales_tax())
2. In-Built Functions (print(), len(), count(), min(), max())
3. Module Functions: modules are a collection of related functions, related
classess, related variables (e.g., we make the bundle of related things)
mdules in python are math
"""

# sum of 2 numbers
def sum(a, b):
    print(a+b)

# calling sum function
sum(3, 4)

# calculate the sales tax
def sales_tax(price):
    new_price=price+(price*0.18)
    return new_price

# calling calc_newPrice function
print(sales_tax(100))

#----------------------------------------------------------------------------#

# Module Functions
# 1
import math # math module

# print(dir(math))
"""
These functions are included in math module:

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb',
'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp',
'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan',
'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians',
'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc',
'ulp']
"""

# now we will use sqrt() using math module
from math import sqrt, log2

print(sqrt(16)) # 4
print(log2(16)) # 4

# 2
import random # random module

print(random.random()) # generates random value from 0 to 1 where 1 is excluded

print(random.randint(1, 10)) # a->b, generates random value in the range, both 1 and 10 are included

#----------------------------------------------------------------------------#

# PRACTICAL EXERCISE 06
# check if number is even or odd
def even_odd(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")

# call function
even_odd(5)

# count the vowels in a string
def count(s):
    cnt=0
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            cnt+=1

    print("Vowels In a String Are: ", cnt)

# calling function
count("Stark")

# print if number is prime or not
def prime(a):
    if a<=1:
        print("Not Prime")

    for i in range(2, a):
        if a%i==0:
            print("Not Prime")
            break

    else:
        print("Prime")

# calling function
prime(5)

# return the average marks of a list of marks

def avg_marks(marks):
    sum=0

    for i in marks:
        sum+=i

    avg=sum/len(marks)
    return avg

# list of marks
marks=[88, 55, 78, 89, 90]
# calling function
print("Average Marks: ", avg_marks(marks))