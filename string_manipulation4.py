"""CHALLENGE 25:
Create a program that reads a person's name from the user. The program should read the name and determine if the name "Silva" appears in the the string.
"""
name = input("Enter a person's name: ")

# Find the index where the name "Silva" starts
index = name.lower().find("silva")

if index != -1 and index != 0 and index != len(name) - len("silva"):
    print("The name 'Silva' is found in the middle of the string.")
else:
    print("The name 'Silva' is not found in the middle of the string.")
