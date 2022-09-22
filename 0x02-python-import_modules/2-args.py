#!/usr/bin/python3

"""
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print(f"{1:d}: {argv[1]:s}")
    else:
        print(f"{len(argv)-1} arguments:")
        for i in range(1, len(argv)):
	        print(f"{i:d}: {argv[i]:s}")
"""
from sys import argv
i = 1

if __name__ == '__main__':
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('1 argument:')
        print('1: {}'.format(argv[1]))
    else:
        print('{:d} arguments:'.format(len(argv) - 1))
        while i < len(argv):
            print('{:d}: {:s}'.format(i, argv[i]))
            i += 1
