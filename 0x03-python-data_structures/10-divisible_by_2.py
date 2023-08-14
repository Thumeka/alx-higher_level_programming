#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = list(range(len(my_list)))

    for d in range(len(my_list)):
        if my_list[d] % 2 == 0:
            new[d] = True
        else:
            new[d] = False

    return new
