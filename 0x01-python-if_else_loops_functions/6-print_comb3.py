#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b:
            print("{}{}".format(a, b), end=', ')
print("\b\b", end='')
