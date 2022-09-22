#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    # no_of_arguments = len(argv)-1
    print(f"{len(argv)-1:d} arguments:")

    for i in range(1, len(argv)):
	    print(f"{i:d}: {argv[i]}")
