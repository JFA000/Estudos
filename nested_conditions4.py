"""CHALLENGE 39:
Create a program that receives a teenager's date of birth and tells them if they have already passed the military enlistment date,
if they are in the year to enlist, or if it is still upcoming.
Also, indicate how much time is left or how much time has already elapsed from the deadline.
"""

import datetime

def check_enlistment_status(date_of_birth):
    today = datetime.date.today()
    age = today.year - date_of_birth.year

    if today < datetime.date(today.year, date_of_birth.month, date_of_birth.day):
        age -= 1

    if age < 18:
        years_remaining = 18 - age
        return f"You are not yet in the period of military enlistment. There are {years_remaining} year(s) left until you turn 18."

    elif age == 18:
        return "This is the year you should enlist in the mandatory military service!"

    else:
        years_passed = age - 18
        return f"You have already exceeded the military enlistment age. It has been {years_passed} year(s) since the deadline."

date_of_birth = input("Enter your date of birth (format: dd/mm/yyyy): ")
day, month, year = map(int, date_of_birth.split("/"))
date_of_birth = datetime.date(year, month, day)

result = check_enlistment_status(date_of_birth)
print(result)
