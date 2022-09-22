#!/usr/bin/python3

import sys
import calculator_1

def main():
    ops = ['+', '-', '*', '/']
    argc = len(argv)

    if (argc - 1) < 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        a, b = int(argv[1]), int(argv[3])
        if argv[2] == '+':
            addition = add(a, b)
            print(f'{a:d} + {b:d} = {addition:d}')
        elif argv[2] == '-':
            diff = sub(a, b)
            print(f'{a:d} - {b:d} = {diff:d}')
        elif argv[2] == '*':
            multiplication = mul(a, b)
            print(f'{a:d} * {b:d} = {multiplication:d}')
        else:
            quotient = div(a, b)
            print(f'{a:d} / {b:d} = {quotient:d}')

if __name__ == "__main__":
    main()