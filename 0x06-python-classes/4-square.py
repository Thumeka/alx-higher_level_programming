#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the atrribute: size"""
        self.size = size

    """Getter"""
    @property
    def size(size):
        return (self.__size)

    """Setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueErroe("size must >= 0")
        self.__size = value

    """Create public instance method"""
    def area(self):
        s_area = self.__size ** 2
        return (s_area)
