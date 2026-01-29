print("****ATM BANKING SYSTEM****\n")
print("IF YOU WANT TO TURN ON THE ATM MACHINE PLEASE ENTER YES  OR NO FOR EXIT\n")
a1=input("ENTER THE YES OR NO:")
g=a1.lower()
balance=50000
if(g=="yes"):
    print("WELCOME TO ATM MACHINE\n")
    print("PLEASE INSERT THE ATM CARD IN MACHINE...")
    number=int(input("\nENTER THE ATM CARD NUMBER:"))
    number1=int(input("\nENTER THE PIN NUMBER OF YOUR ACCOUNT:"))
    while True:
        print("1.CHECK BALANCE")
        print("\n2.DEPOSIT OF MONEY")
        print("\n3.WITHDRAW MONEY FOR YOUR ACCOUNT")
        print("\n4.EXIT FOR YOUR ACCOUNT")
        num1=int(input("ENTER A NUMBER BY YOUR CHOOSE:"))
        if(num1==1):
            numb1=int(input("ENTER THE PIN NUMBER:"))
            while(number1!=numb1):
                print("INCORRECT PIN NUMBER..")
                numb1=int(input("ENTER THE PIN NUMBER:"))
            print("YOUR BALANCE IN OUR BANK ACCOUNT IS:",balance)
        elif(num1==2):
            num2=int(input("PLEASE ENTER THE DEPOSIT MONEY IN YOUR ACCOUNT:"))
            print("\nOK PLEASE WAIT....")
            numb1=int(input("ENTER THE PIN NUMBER:"))
            while(number1!=numb1):
                print("PLEASE THE CORRECT PIN CODE TO DEPOSIT..😒")
                numb1=int(input("ENTER THE PIN NUMBER:"))
            print("\nTHE ENTERED AMOUNT IS SUCCESSFULLY DEPOSIT IN YOUR ACCOUNT..")
            balance=balance+num2
        elif(num1==3):
            num3=int(input("ENTER THE WITHDDRAW AMOUNT FROM YOUR ACCOUNT:"))
            print("OK PLEASE WAIT FOR FEW MINUTES🕐")
            numb1=int(input("ENTER THE PIN NUMBER:"))
            while(number1!=numb1):
                numb1=int(input("PLEASE ENTER THE CORRECT PIN NUMBER:"))
            print("THE PIN NUMBER IS SUCCESSFULLY MATCHED...😍😎")    

            while(num3>balance):
                print("THE AMOUNT YOU HAVE ENTERED IS MORE THAN YOUR BALANCE")
                num3=int(input("ENTER THE WITHDDRAW ACOUNT FROM YOUR ACCOUNT:"))
            balance=balance-num3
        elif(num1==4):
            print("THANKYOU FOR USING YOUR ATM MACHINE...😍😎👌\n")
            print("VISIT AGAIN!....🫡😍👍")   
            break
        else:
            print("WASTEFELLOW  GA AA NUMBER ECHANURA NIKU ")
            print("1 TO 4 LO AO NUMBERS DSELECT CHEYSUKO RA RAJA...")

else:
    print("exiting for the atm machine")

        
