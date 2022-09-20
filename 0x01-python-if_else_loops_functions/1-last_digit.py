#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if number < 0:
    if last_digit == 0:
        last_digit = last_digit
        print(f"Last digit of {number:d} is {last_digit:d} and is {last_digit:d}")
    else:
        last_digit = -abs(last_digit)
        print(f"Last digit of {number:d} is {last_digit:d} \
and is less than 6 and not 0")
else:
     if last_digit == 0:
        print(f"Last digit of {number:d} is {last_digit:d} and is {last_digit:d}")
     elif last_digit <= 5:
        print(f"Last digit of {number:d} is {last_digit:d} \
and is less than 6 and not 0")
     else:
        print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
