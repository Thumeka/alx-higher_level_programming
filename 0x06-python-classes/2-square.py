#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    """Class Square definition"""

    def __init__(self, size=0):
        """
        Initializes square

        Atrributes:
            __size (int): size of square 0 if none
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
