#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter, and
displays the body of the response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    mail = {'email': argv[2]}
    requ = requests.post(url, data=mail)
    print(requ.text)
