"""CHALLENGE 32:
Create a program that reads any year input by the user and informs the user whether that year is a leap year.
"""
print("""Explanation of leap year calculation:

"Step 1. If a year is evenly divisible by 4, go to step 2. Otherwise, it is not a leap year."
"Step 2. If a year is evenly divisible by 100, go to step 3. Otherwise, it is a leap year."
"Step 3. If a year is evenly divisible by 400, it is a leap year. Otherwise, it is not a leap year.""")

year = input("Enter a year: ")
while not year.isdigit():
    year = input("Invalid input. Please enter a valid year: ")

year = int(year)

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0

if divisible_by_4:
    if divisible_by_100:
        if divisible_by_400:
            print(f"The year {year} is a leap year because it is divisible by 4, 100, and 400.")
        else:
            print(f"The year {year} is not a leap year because it fails at step 3.")
    else:
        print(f"The year {year} is a leap year because it is divisible by 4 and not divisible by 100.")
else:
    print(f"The year {year} is not a leap year because it fails at step 1.")
