#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = set(my_list)
    tot_sum = 0
    for i in uniq_sum:
        tot_sum += i
    return tot_sum
