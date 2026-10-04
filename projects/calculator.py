# PRACTICAL EXERCISE 03
# Mini-Project
# Calculator that perform some basic calculations

num1=int(input("Enter First Number: "))
opt=input("Enter Operator (+, -, *, /, %, **): ")
num2=int(input("Enter Second Number: "))

if opt=='+':
    print("Addition: ", num1+num2)

elif opt=='-':
    print("Sutraction: ", num1-num2)

elif opt=='*':
    print("Multiplication: ", num1*num2)

elif opt=='/':
    print("Division: ", num1/num2)

elif opt=='%':
    print("Modulus: ", num1%num2)

elif opt=='**':
    print("Exponent/Power: ", num1**num2)

else:
    print("Please Choose Operator Between (+, -, *, /, %, **)")        
