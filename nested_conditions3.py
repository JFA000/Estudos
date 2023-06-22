"""CHALLENGE 38:
Write a program that receives two integers and compares them, showing the larger integer. 
"""

value1 = int(input("Enter first integer: "))
value2 = int(input("Enter second integer: "))



if value1 > value2:
    print(f"The largest number is {value1}.")
elif value1 < value2:
    print(f"The largest number is {value2}.")
else:
    print("Both numbers are equal.")