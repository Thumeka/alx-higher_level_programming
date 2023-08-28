#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    safe = 0
    for i in range(x):
        try:
            print(f"{my_list=[safe]}", end="")
        except IndexError:
            break
        safe += 1
    print()
    return safe
