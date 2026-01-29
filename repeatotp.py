import random
num1=random.randint(1207,58907)
print("the otp is:",num1)
num2=int(input("enter the correct otp:"))
while(num1!=num2):
    num1=random.randint(1207,58907)
    print("the otp is:",num1)
    print("incorrect otp")
    num2=int(input("enter the correc otp:"))

print("logined sucessfully")
