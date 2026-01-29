
print("MY COOL DRINK SHOP \n 1 THUMB UP COOL DRINK $30 \n 2 SPRITE COOL DRINK $32 \n 3 FANTA COOL DRINK $21")
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
total=sum(list)
print("your total amount in our shop:",total)
payment=int(input("enter the given amount by our shop:"))
com=total-payment
if total==payment:
    print("ok! you enter the correct amount,thank you visit again")
elif total>payment:
    print("the total bill is more than your payment sorry please pay the remaining bill is $",com)
    a=int(input("enter the remaining amount:"))
    if com==a:
        print("thank you for enter the remaining amount")
    elif com>a:
        print("sorry please enter the remaining bill or amount",com-a)
    elif com<a:
        print("thank you entering more than your bill:",a-com)           
elif total<payment:
   print("thank you for paying more amount ,thankyou visit again the extra amount paid by person")               
else:
    print("invalid number or alphabet please enter the total bill given by our shop")

print("thank you for interest for buying in my shop")    
    

    