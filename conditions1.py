"""CHALLENGE 28:
Your task is to create a Python program that simulates a number guessing game. The program should randomly generate a number between 1 and 5, and the user will have to guess that number correctly.
"""
from random import randrange

num = int(randrange(0,6))
#print(num)
answer = int(input("Let's play a game, I'm going to think of a number between 0 and 5 and you will try to guess which number I'm thinking about."
               "\nSo, what's your guess?\n"))
if answer == num:
    print(f"Yes, {answer} is the number I was thinking about, Congratulations!")
else:
    print(f"No, {answer} is not the number I was thinking about, I was thinking about {num}!")

