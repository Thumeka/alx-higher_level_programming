#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Write a function that reads a text file, prints to stdout"""
    with open(filename) as f:
        for content in f:
            print(content, end="")
