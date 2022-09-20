#!/usr/bin/python3
for letter in map(chr, range(ord('a'), ord('z')+1)):
    if letter not in "qe":
        print("{}".format(letter), end='')
