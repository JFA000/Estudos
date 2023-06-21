"""CHALLENGE 37:
Write a program that converts a integer to binary, octal or hexadecimal. 
"""

value = int(input("Enter a integer you want to convert: "))
conversion = int(input("Forms of conversion\n1 - Binary\n2 - Octal\n3 - Hexadecimal\n\nSelect your form of conversion: "))

if conversion == 1:
    print(f"Binary: {bin(value)[2:]}")
elif conversion == 2:
    print(f"Octal: {oct(value)[2:]}")
else:
    print(f"Hexadecimal: {hex(value)[2:].upper()}")