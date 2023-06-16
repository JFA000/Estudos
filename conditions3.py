"""CHALLENGE 30:
Make a program that receives a integer. Output if they are even or odd.
"""
integer = input("Enter any integer: ")

while not integer.isdigit():
    integer = input("Invalid input. Please enter an integer: ")

integer = int(integer)

if integer % 2 == 0:
    number_type = "even"
else:
    number_type = "odd"
print(f"{integer} is an {number_type} number.")

