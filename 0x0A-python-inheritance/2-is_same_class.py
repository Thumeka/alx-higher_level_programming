#!/usr/bin/python3
"""Returns True if the object is exactly an instance or False"""


def is_same_class(obj, a_class):
    """Write a function that returns True or False"""
    if type(obj) == a_class:
        return True
    else:
        return False
