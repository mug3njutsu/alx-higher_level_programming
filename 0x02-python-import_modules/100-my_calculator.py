#!/usr/bin/python3

import sys
from calculator_1 import add,sub,div,mul

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        if operator == "+":
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "/":
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        elif len(operator) != 1:
            a = int(sys.argv[1])
            b = int(sys.argv[-1])
            print("{} {} {} = {}".format(a, "*", b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
