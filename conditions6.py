"""CHALLENGE 33:
Create a program that reads three numbers and show the smallest and the largest.
"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"The smallest number is: {min(num1, num2, num3)}")
print(f"The largest number is: {max(num1, num2, num3)}")
