#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    mail = {'q': letter}
    requ = requests.post(url, data=mail)

    try:
        dic = requ.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
