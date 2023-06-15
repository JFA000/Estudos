"""CHALLENGE 24:
Write a program that prompts the user to enter the name of their city and determine if the city name starts with the word "Santo" or not.
"""
city_name = input("Enter your city name: ")

if city_name[:5].lower() == "santo":
    print("The city name starts with 'Santo'.")
else:
    print("The city name does not start with 'Santo'.")
