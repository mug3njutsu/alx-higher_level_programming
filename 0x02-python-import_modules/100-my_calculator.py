#!/usr/bin/python3

import sys
from calculator_1 import add,sub,mul,div

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	elif sys.argv[2] not in "+-*/":
		print("Unknown operator. Available operators: +, -, * and /")
		exit(1)
	else:
		result = eval("".join(sys.argv[1:4]))
		print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")