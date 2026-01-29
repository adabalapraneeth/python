import random
pa=random.randint(10000,66666)
print("THE ONE TIME PASSWORD TO CONTINUE THE CALCULATOR:",pa)
otp=int(input("ENTER THE GIVEN OTP:"))
if pa==otp:
    print("SIMPLE CALCULATOR")
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    opertor=(" SIMPLE CALCULATOR\n 1 addition\n 2 subtraction\n 3 multipcation\n 4 division\n 5 exit")
    print(opertor)
    inputoperator=int(input("enter the number that what you want to perform between two numbers:"))
    if inputoperator==1:
        print("sum of two numbers:",a+b)
    elif inputoperator==2:
        print("subraction of two numbers:",a-b)
    elif inputoperator==3:
        print("multipcation between two numbers:",a*b)
    elif inputoperator==4:
        print("division between two numbers:",a/b)
    elif inputoperator==5:
        print("ok your are exiting the calculator.......")
else:
    print("invalid otp")                    
         
