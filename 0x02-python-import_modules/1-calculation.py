#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

if __name__ == "__main__"
    a = 10
    b = 5

    addition = add(a, b)
    diff = sub(a, b)
    multiplication = mul(a, b)
    quotient = div(a, b)

    print(f"{a:d} + {b:d} = {addition}")
    print(f"{a:d} - {b:d} = {diff}")
    print(f"{a:d} * {b:d} = {multiplication}")
    print(f"{a:d} / {b:d} = {quotient}")
