#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    while len(my_list) != 1:
        my_list.remove(min(my_list))
    return my_list[0]
