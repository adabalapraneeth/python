import random
account_number=[]
name=[]
age=[]
year=[]
balance=[]
PIN=[]
def value_1():
    print("CREATING AN ACCOUNT IN BANK..")
    c1=input("ENTER YOUR NAME:")
    name.append(c1)
    c2=int(input("ENTER YOUR AGE:"))
    age.append(c2)
    c3=int(input("ENTER YOUR DATE OF BIRTH YEAR:"))
    year.append(c3)
    account_num=random.randint(1000000000,9999999999)
    P1=int(input("CREATE A PIN TO YOUR ACCOUNT:"))
    PIN.append(P1)
    print("YOUR ACCOUNT NUMBER GIVEN BY THE BANK:",account_num)
    account_number.append(account_num)
    B1=int(input("ENTER THE AMOUNT IN YOUR ACCOUNT:"))
    balance.append(B1)
def value_2():
    print("CREATED ACCOUNT IN THE BANK")
    for i in range(len(PIN)):
        print("\nTHE NAME OF ACCOUNT CREATOR:",name[i])
        print("\nTHE ACCOUNT NUMBER:",account_number[i]) 
        print("\nTHE PIN CREATED BY CREATOR:",PIN[i])
def value_3():
    T1=int(input("ENTER THE ACCOUNT NUMBER FROM WHICH YOU WANT TO TRANSACTION:"))
    for i in range(len(PIN)):
        if(account_number[i]==T1):
            print("\nTHE ACCOUNT IS CREATED BY THE NAME:",name[i])
            print("\nTHE AGE OF THE CREATOR :",age[i])
            print("\nTHE PIN OF THE ACCOUNT CREATOR:",PIN[i])
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            while True:
                print("\n1.WITHDRAW FROM MY ACCOUNT")
                print("\n2.DEPOSIT AMOUNT TO MY ACCOUNT")
                print("\n3.TRANSACTION OF MY MONEY TO ANOTHER ACCOUNT")
                print("\n4.BALANCE IN THE PRESENT ACCOUNT")
                print("\n5.EXIT")
                T2=int(input("CHOOSE AN OPTION:"))
                if(T2==1):
                    print("THE AMOUNT IN THE PRESENT ACCOUNT IS:",balance[i])
                    W1=int(input("ENTER THE AMOUNT WHICH YO WANT TO WITHDRAW:"))
                    while(balance[i]<W1):
                        print("THE AMOUNT YOU ENTERED IN THE INPUT IS MORE THAN YOUR BALANCE")
                        W1=int(input("PLEASE ENTER THE CORRECT AMOUNT THAT SHOULD BE MUST LESS THAN YOUR BALANCE:"))
                    balance[i]=balance[i]-W1
                    print("THE AMOUNT PRESENT IN YOUR ACCOUNT IS:",balance[i])
                elif(T2==2):
                    print("THE AMOUNT PRESENT IN YOUR ACCOUNT:",balance[i])
                    D1=int(input("ENTER THE AMOUNT TO DEPOSIT IN YOUR ACCOUNT:"))
                    while(D1<0):
                        print("\nSORRY  YOU HAVE ENTERED A NEGATIVE NUMBER.")
                        D1=int(input("PLEASE ENTER THE VALID AMMOUNT TO DEPOSIT"))
                    balance[i]=balance[i]+D1
                    print("THE BALANCE IN YOUR ACCOUNT:",balance[i])
                elif(T2==3):
                    print("THE PRESENT ACCOUNT NUMBER WORKING IN THE SYSTEM:",account_number[i])
                    for j in range(len(PIN)):
                        if(account_number[j]==account_number[i]):
                            continue
                        else:
                            print("THE ACCOUNT NUMBERS TO TRANSFER FROM YOUR ACCOUNT TO ANOTHER ACCOUNT:",account_number[j])
                    print("THE AMOUNT PRESENT IN YOUR ACCOUNT IS:",balance[i])
                    T3=int(input("ENTER THE ACCOUNT NUMBER WHICH YOU WANT TO TRANSFER:"))
                    for k in range(len(PIN)):
                        if(account_number[k]==T3):
                            T4=int(input("ENTER THE TRANSCATION AMOUNT FROM YOUR ACCOUNT TO ANOTHER ACCOUNT:"))
                            while(T4>balance[i]):
                                print("SORRY MORE AMOUNT YOU HAVE ENTERED COMPARED TO YOUR BALANCE..")
                                print("THE AMOUNT PRESENT IN YOUR AMOUNT IS:",balance[i])
                                T4=int(input("PLEASE ENTER THE CORRECT AMOUNT THAT SHOULD BE LESS THAN BALANCE: "))
                            P1=int(input("ENTER THE PIN NUMBER OF YOUR ACCOUNT:"))
                            while(P1!=PIN[i]):
                                print("U HAVE ENTERED THE WRONG PIN NUMBER")
                                P1=int(input("PLLEASE ENTER THE CORRECT PIN OF YOUR ACCOUNT:"))
                            balance[i]=balance[i]-T4
                            balance[k]=balance[k]+T4
                            print("\nTHE AMOUNT PRESENT IN YOUR ACCOUNT AFTER THE TRANSACTION:",balance[i])
                            print("\nTHE AMOUNT PRESENT THE IN  THE ANOTHER PERSON ACCOUNT:",balance[k])
                elif(T2==4):
                    B1=int(input("ENTER THE PIN NUMBER TO CHECK THE BALANCE:"))
                    while(B1!=PIN[i]):
                        print("SORRY TO SAY U HAVE ENTERED THE WRONG PIN...")
                        B1=int(input("ENTER THE CORRECT PIN NUMBER:"))
                    print("\nTHE AMOUNT PRESENT IN THE OPENDED ACCOUNT IS:",balance[i]) 
                elif(T2==5):
                    print("\nTHANK YOU FOR OPENING THE BANK ACCOUNT IN THE BANK.")
                    print("\nYOUR EXIT FOR THE TRANSACTION SECTION.") 
                    break
while True:
    print("***WELCOME TO THE BANK***")
    print("\n1.CREATING ACCOUNT IN THE BANK")
    print("\n2.DISPLAYING ACCOUNTS PRESENT IN THE BANK")
    print("\n3.TRANSACTION OF MONEY FROM ONE ACCOUNT TO ANOTHER ACCOUNT")
    print("\n4.EXIT")
    value=int(input("ENTER A VALUE OR OPTION:"))
    if(value==1):
        value_1()
    elif(value==2):
        value_2()
    elif(value==3):
        value_3()
    elif(value==4):
        print("\nTHANK YOU FOR VISITING THE BANK")
        print("\nVISIT AGAIN")
        break
    else:
        print("\nPLEASE ENTER THE NUMBER FROM 1 TO 4 ONLY")






    
    
           
       




