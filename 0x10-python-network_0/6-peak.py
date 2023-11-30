#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    li = list_of_integers
    begi = 0
    end = len(li)-1

    if li[begi] > li[begi+1]:
        return l[begi]
    if li[end] > l[end-1]:
        return l[end]

    mid = (begi+end)//2
    if li[mid-1] < l[mid] and li[mid+1] < li[mid]:
        return li[mid]
    if li[mid] < li[mid-1]:
        return find_peak(li[begi:mid+1])
    elif li[mid] < li[mid+1]:
        return find_peak(li[mid:end+1])
    else:
        return li[begi]
