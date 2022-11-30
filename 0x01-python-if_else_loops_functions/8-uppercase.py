#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}".format(chr(ord(str[i])-32)), end="")
        else:
            print("{}".format(chr(ord(str[i]))), end="")

        i = i + 1
