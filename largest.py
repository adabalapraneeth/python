number=input("enter the numbers by giving space:")
numbers=number.split()
list_of_numbers=[int(item) for item in numbers]
list_of_numbers.sort()
set_a=set(list_of_numbers)
list1=[red for red in set_a]
list1.sort()
print("first largest number:",list1[-1])
print("second largest number:",list1[-2])
