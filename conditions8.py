"""CHALLENGE 35:
Create a program that reads the length of three parallel lines and tells the user if they can or cannot form a triangle
"""
print(""""Condition of existence of a triangle: 
"Given three line segments, they cannot always form a triangle.
For the three segments to form a triangle, there is what we know as the condition of existence,
which is as follows: the sum of two sides is always less than the third side"

a + b > c
b + c > a
a + c > b

""")

a = float(input("Enter the length of the first line: "))
b = float(input("Enter the length of the second line: "))
c = float(input("Enter the length of the third line: "))

if a >= b + c:
    print(f"The first line ({a}) is greater than or equal to the sum of the other two lines ({b} + {c} = {b+c}). These lines cannot form a triangle.")
elif b >= a + c:
    print(f"The second line ({b}) is greater than or equal to the sum of the other two lines ({a} + {c} = {a+c}). These lines cannot form a triangle.")
elif c >= a + b:
    print(f"The third line ({c}) is greater than or equal to the sum of the other two lines ({a} + {b} = {a+b}). These lines cannot form a triangle.")
else:
    print("These lines can form a triangle.")


