#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to
the URL and displays the value of the variable X-Request-Id
in the response head"""
import requests
from sys import argv


if __name__ == "__main__":
    requ = requests.get(argv[1])
    print(requ.headers.get('X-Request-Id'))
