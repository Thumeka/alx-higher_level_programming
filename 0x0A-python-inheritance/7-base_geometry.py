#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """Defines methods of BaseGeometry"""
    def area(self):
        """Area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
