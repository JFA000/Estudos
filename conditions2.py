"""CHALLENGE 29:
Make a program that receives the speed in which a car is travelling in km/h. If the car is faster than allowed, calculate a fee and show it to the user.
"""

speedlimit = 80
carspeed = float(input("Safety first while in the highway!\nEnter the car current speed in km/h: "))
fee  = 7

if carspeed > 80:
    print(f"Your car speed of {carspeed}km/h is above the limit of {speedlimit}km/h in the highway! Pay a fee of R${fee:.2f} for each km above {speedlimit}km/h.\n"
          f"Your total fee is R${((carspeed-speedlimit)*fee):.2f}.")
else:
    print(f"Your car speed of {carspeed}km/h is below the limit of {speedlimit}km/h in the highway, safe travels!")

