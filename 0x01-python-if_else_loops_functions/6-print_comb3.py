#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b:
            if f"{a}{b}" != "89":
                print("{}{}".format(a, b), end=', ')
            else:
                print("{}{}".format(a, b), end='')
