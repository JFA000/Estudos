"""CHALLENGE 34:
Create a program that reads a salary and increases it by 10% if it is higuer than R$1250 and by 15% if it is lower or equal to that.
"""
salary = input("Enter your salary: ")

while True:
    try:
        salary = float(salary)
        break
    except ValueError:
        salary = input("Wrong input, please enter your salary: ")

adjusted_salary = salary * 1.15 if salary <= 1250 else salary * 1.10

print(f"The adjusted salary is: {adjusted_salary:.2f}")
