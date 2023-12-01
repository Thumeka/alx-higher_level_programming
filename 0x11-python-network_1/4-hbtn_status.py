#!/usr/bin/python3
"""fetches the request using intranet using urllib"""
import requests


if __name__ == "__main__":
    requ = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(requ.text)))
    print("\t- content: {}".format(requ.text))
