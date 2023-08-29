#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Instantiation with optional private instance attribute"""
        if tpe(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Public instance method"""
    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        return (self.__size)**2
