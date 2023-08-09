#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) >= ord('a')) and (ord(c) <= ord('z')):
            letter = chr(ord(letter)-ord('a')+ord('A'))
    print("{}".format(letter), end='')
    print()
