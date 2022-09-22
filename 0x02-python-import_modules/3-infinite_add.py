#!/usr/bin/python3

import sys

if __name__ == "__main__":
    numbers = sys.argv[1:]
    content = [int("".join(i)) for i in numbers]
    print(sum(content))
