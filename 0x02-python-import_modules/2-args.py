#!/usr/bin/python3

import sys

def main():
	no_of_arguments = len(sys.argv)-1
	print(f"{no_of_arguments:d} arguments.")

	for i in range(1, len(sys.argv)):
		print(f"{i:d}: {sys.argv[i]}")

if __name__ == "__main__":
	main()
