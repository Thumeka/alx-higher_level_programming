#!/usr/bin/python3
"""Module 1-write_file"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file (UTF8);
    and returns the number of characters written"""
    with open(filename, 'w') as f:
        return f.write(text)
