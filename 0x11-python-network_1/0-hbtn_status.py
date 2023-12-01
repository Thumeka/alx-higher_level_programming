#!/usr/bin/python3
"""fetches the intranet using urllib"""
import urllib.request


if __name__ == "__main__":
    requ = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(requ) as response:
        Page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(Page)))
        print("\t- content: {}".format(Page))
        print("\t- utf8 content: {}".format(Page.decode("utf-8")))
