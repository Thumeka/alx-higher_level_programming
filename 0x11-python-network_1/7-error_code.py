#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response"""
import requests
from sys import argv


if __name__ == "__main__":
    requ = requests.get(argv[1])
    if requ.status_code >= 400:
        print("Error code: {}".format(requ.status_code))
    else:
        print(requ.text)
