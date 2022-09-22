#!/usr/bin/python3
"""
from calculator_1 import add,sub,div,mul
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            print("{} + {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "/":
            print("{} / {} = {}".format(a, operator, b, div(a, b)))
        elif operator == "*":
            print("{} * {} = {}".format(a, operator, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
"""
if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
