#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lis = 0
    while lis < x:
        try:
            print("{}".format(my_list[lis]), end="")
        except IndexError:
            break
        lis += 1
    print("")
    return lis
