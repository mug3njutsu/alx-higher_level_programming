#!/usr/bin/python3

def islower(c):
    for char in c:
        if char in list(map(chr, range(ord('a'), ord('z')+1))) and char not in "":
            return True
