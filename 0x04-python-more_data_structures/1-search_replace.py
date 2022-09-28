#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    find_index = new_list.index(search)
    new_list[find_index] = replace
    return new_list
