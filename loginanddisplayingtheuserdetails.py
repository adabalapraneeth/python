import random
print("WELCOME TO MY WEBSITE.\n")
arr=[]
lem=[]
while True:
    print("___________________________")
    print("1.CREATING A ACCOUNT IN MY WEBSITE.\n")
    print("2.DISPLAYING THE  STORED ACCOUNTS.\n")
    print("3.EXIT\n")
    a1=int(input("ENTER A NUMBER:"))
    if(a1==1):
        a=input("ENTER THE NAME OF THE USER:")
        b=int(input("ENTER THE PHONE NUMBER OF THE USER:"))
        c1=random.randint(1000,9999)
        print(f"THE OTP WILL SEND TO THE PHONE NUMBER:{b}\n")
        print("THE OTP IS ALREADY SENT TO YOUR YOUR PHONE NUMMBER PLLEASE CHECK\n")
        print("THE OTP IS:",c1)
        otp=int(input("ENTER THEOTP SENDED TO U:"))
        while(c1!=otp):
            c1=random.randint(1000,9999)
            print(f"THE OTP WILL SEND TO THE PHONE NUMBER:{b}\n")
            print("THE OTP IS ALREADY SENT TO YOUR YOUR PHONE NUMMBER PLLEASE CHECK\n")
            print("THE OTP IS:",c1)
            otp=int(input("ENTER THEOTP SENDED TO U:"))
        if(c1==otp):
            print("CREATING THE ACCOUNT IS SUCCESFULLY COMPLETED...")
            arr.append(a)
            lem.append(b) 
    if(a1==2):
        for i in range(len(arr)):
            if(len(arr)==0):
                print("NO ACCOUNT IS PRESENT IN THE LOGIN PAGE.. SO CREATE AN ACCOUNT")
            else:    
                print(f"AN ACCOUNT HAS CREATED WITH AN USER NAME: {arr[i]} AND WITH THE PHONE NUMBER: {lem[i]}")
                print("THANKYOU FOR CREATING THE ACCOUNTS IN MY WEBSITE😍😎😎😎😎.")  
    if(a1==3):
        print("THANK YOU FOR WATCHING MY WEBSITE.\n")
        print("YOUR EXITING FROM MY WEBSITE....❤️")
        break             

