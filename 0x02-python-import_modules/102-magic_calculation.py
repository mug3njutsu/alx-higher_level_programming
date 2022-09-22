#!/usr/bin/python3
import magic_calculation_102

def magic_calculation(a, b):
    if a < b:
        c = magic_calculation.add(a, b)
        for i in range(4, 6):
            c = magic_calculation.add(c, i)
        return c
    else:
        return (magic.calculation.sub(a, b))

