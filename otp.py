import random
otp=random.randint(10000, 999999)
print("ONE TIME PASSWORD:",otp)
a=int(input("enter the OTP:"))
if otp==a:
    print("correct otp")
else:
    print("incorrect otp")        
