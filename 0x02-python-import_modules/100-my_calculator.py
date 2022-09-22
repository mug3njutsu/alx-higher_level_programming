#!/usr/bin/python3

import sys
from calculator_1 import add,sub,mul,div

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	else:
		print(sys.argv)