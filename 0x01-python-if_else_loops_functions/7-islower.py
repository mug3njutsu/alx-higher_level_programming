#!/usr/bin/python3

def islower(c):
    if c in list(map(chr, range(ord('a'), ord('z')+1))):
        return True
    else:
        return False
