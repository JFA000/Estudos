"""CHALLENGE 40:
Create a program that reads two grades of a student, calculates their average, and displays a message of approval or failure for grades below a limit set by you.
"""

def calculate_grade_average(grade1, grade2):
    average = (grade1 + grade2) / 2
    return average

def check_approval_status(average):
    if average < 5:
        return "Sorry, you have failed."
    elif average >= 5 and average < 7:
        return "You are in Recovery."
    else:
        return "Congratulations! You have passed."

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))

average = calculate_grade_average(grade1, grade2)
result = check_approval_status(average)
print(result)
