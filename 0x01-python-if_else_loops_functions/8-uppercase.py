#!/usr/bin/python3
def uppercase(str):
    new = ""
    for letter in s:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - ord('a') + ord('A'))
        new += letter
    print("{}".format(new))
