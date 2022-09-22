#!/usr/bin/python3

import sys

def main():
	result = ""
	numbers = sys.argv[1:]
	content = [int("".join(i)) for i in numbers]
	print(sum(content))

if __name__ == "__main__":
	main()