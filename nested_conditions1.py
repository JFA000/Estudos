"""CHALLENGE 36:
Write a program to approve the bank loan for the purchase of a house.
The program should ask the value of the house, the buyer's salary and how many years he will pay.
Calculate the monthly installment, knowing that it cannot exceed 30% of the salary or else the loan will be denied.
"""

def get_input(message):
    # This function asks the user for an input and validates it, receiving only numbers.
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("Invalid input. The value must be positive.")
        except ValueError:
            print("Invalid input. The value must be a number.")

salary = get_input("Enter your monthly salary: R$")
price = get_input("Enter the price of the house you want to buy: R$")
years = get_input("Enter how many years you would like to pay for the house: ")

paymax =  salary * 0.30
monthlypay = price / (years * 12)

if monthlypay > paymax:
    print(f"You cannot buy the house. Your monthly pay should be at least R${monthlypay:.2f} to pay the house in {years} years.")
else:
    print(f"Installment accepted, your monthly payment will be R${monthlypay:.2f}.")
