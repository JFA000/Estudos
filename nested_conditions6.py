"""CHALLENGE 41:
Create a program that receives the year of birth of an athlete and tell them in which sports category they currently belong to.
"""

from datetime import datetime

current_year = datetime.now().year
birth_year = int(input("Enter your year of birth: "))
age = current_year - birth_year

if age <= 9:
    category = "Child"
elif age <= 14:
    category = "Youth"
elif age <= 19:
    category = "Junior"
elif age <= 20:
    category = "Senior"
else:
    category = "Master"

print(f"You are currently in {category}.")
