num1=input("enter the binary number:")
sum=0
value=0
num2=num1[::-1]
for i in num2:
    sum=sum+int(i)*(2**value)
    value=value+1   

print("the decimal number  system is",sum)

