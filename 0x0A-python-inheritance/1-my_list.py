#!/usr/bin/python3
"""Module contains MyList"""


class MyList(list):
    """Write a class MyList that inherits from list"""
    def print_sorted(self):
        """Public instance method and list in ascending order"""
        print(sorted(self))
