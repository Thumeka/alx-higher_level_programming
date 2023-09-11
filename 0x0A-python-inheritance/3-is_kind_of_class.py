#!/usr/bin/python3
"""Module is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Write a function that returns True if the object is an instance;
    object is an instance of a class that inherited from;
    otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
