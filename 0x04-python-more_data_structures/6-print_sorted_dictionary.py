#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.keys())
    for k in sort_dict:
        value = a_dictionary[k]
        print(f"{k}: {value}")
