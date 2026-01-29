# NUMBER GAME
print("***...LUCKY NUMBER GAME...***")
#N=int(input("enter the stoping number:"))
import random
num1=random.randint(1,999)
num2=int(input("enter the number  from 1 to 999:"))
if num1==num2:
    print("absolutely right the guess number is right")
    print("congrats you won the game")
    print("the given value by computer:",num1)
elif num1>num2:
    print("the given number by the computer is more than  your enter number") 
    print("sorry you lose the game")
    print("the given value by computer:",num1)
elif num1<num2:    
    print("the enter number by you is more than computer value")
    print("sorry you lose the game") 
    print("the given value by computer:",num1)     
