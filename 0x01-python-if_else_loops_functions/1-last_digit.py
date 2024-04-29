#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_d = (((number * -1) % 10) * -1)
elif number == 0:
    last_d = number
else:
    last_d = number % 10
print(f"Last digit of {number} is {last_d} and is ", end="")
if last_d > 5:
    print("greater than 5")
elif last_d < 6 and last_d != 0:
    print("less than 6 and not 0")
elif last_d == 0:
    print("is 0")
