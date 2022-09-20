#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = -number
    last = int(str(number)[-1])
    print(last, end="")
    return last
