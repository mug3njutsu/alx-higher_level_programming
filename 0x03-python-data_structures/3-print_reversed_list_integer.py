#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for a in range(-1, -abs(len(my_list)+1), -1):
        print(my_list[a])