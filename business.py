words=("WELCOME TO MY SHOP\n MENU\n 1 THUMBSUP COOL DRINK $30\n 2 SPRITE COOL DRINK $32\n 3 ARTOS  COOL DRINK $21\n 4 COCO COLA COOL DRINK $9\n 5 BURGER $4\n 6 CHICKEN BURGER $4\n 7 CHICKEN WINGS $8")
print(words)
num=input("enter what you want to buy in menu items enter number by givening space:")
num2=num.split()
num3=[int(item)for item in num2]
list=[]
for item in num3:
    if item==1:
        list.append(30)
    elif item==2:
        list.append(32)
    elif item==3:
        list.append(21)    
    elif item==4:
        list.append(9)
    elif item==5:
        list.append(4) 
    elif item==6:
        list.append(4)
    elif item==7:
        list.append(8)           
total=sum(list)
print("your total amount in our shop:",total)
payment=int(input("enter the given amount by our shop:"))
while(payment<total):
    print("transaction is failed, because the amount entered is less than your bill")
    print("your total amount in our shop:",total)
    payment=int(input("enter the given amount by our shop:"))

if(payment==total):
    print("thank you for paying the total bill")
    print("thank you visit again....")
elif(payment>total):
    print("thank you for paying extra amount:",payment-total) 
    print("thank you visit again...")   
    
