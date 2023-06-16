"""CHALLENGE 31:
Create a program that computes the distance of a journey in kilometers and determines the corresponding fare.
The user will be charged R$0.50 for each kilometer for trips up to a maximum distance of 200 kilometers.
For longer journeys, the fare per kilometer will be reduced to R$0.40.
"""
distance = float(input("Enter the distance of the journey in kilometers: "))

if distance <= 200:
    fare = distance * 0.50
else:
    fare = distance * 0.40

print("The fare for the journey is R$",fare)
