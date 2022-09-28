#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    final = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    for key in final:
        print(f"{key}: {final[key]}")
