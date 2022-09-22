#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"{len(argv)-1:d} arguments.")
    elif len(argv) < 3:
        print(f"{len(argv)-1:d} argument:")
        print(f"{1:d}: {argv[1]}")
    else:
        print(f"{len(argv)-1:d} arguments:")
        for i in range(1, len(argv)):
	        print(f"{i:d}: {argv[i]}")
