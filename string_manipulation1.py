"""CHALLENGE 22:
The challenge is to create a program that reads a person's full name and displays:
» The name with all lowercase letters.
» The name with all uppercase letters.
» The total number of letters (excluding spaces).
» The number of letters in the first name.
"""
name = string = input("Enter your name: ")
print(f"Name in uppercase = {name.upper()}")
print(f"Name in lowercase = {name.lower()}")
letter_count = sum(1 for char in name if char.isalpha())
print(f"Letters in name = {letter_count}")
splited_name = name.split()
letter_count = sum(1 for char in splited_name[0] if char.isalpha())
print(f"Letters in first name = {letter_count}")