#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ''
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_str += chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_str += char

    print(uppercase_str)
