"""CHALLENGE 23:
The challenge is to create a program that reads a four-digit number and displays each digit separately.
"""
number = input("Enter a four-digit number: ")
while not number.isdigit() or len(number) != 4:
    print("Invalid input. Please enter a valid four-digit number.")
    number = input("Enter a four-digit number: ")
number.split
i = 0
while i <4:
    print(f"The digit at position {i+1} is: [{number[i]}]")
    i +=1
