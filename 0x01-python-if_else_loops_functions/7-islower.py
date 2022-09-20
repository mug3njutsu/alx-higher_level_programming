#!/usr/bin/python3

def islower(c):
    for char in c:
        if char in list(map(chr, range(ord('a'), ord('z')))):
            return True
