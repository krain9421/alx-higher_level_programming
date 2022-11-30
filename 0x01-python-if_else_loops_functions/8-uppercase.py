#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (True)
    else:
        return (False)


def uppercase(str):
    i = 0
    while i < len(str):
        c = ord(str[i])
        print("{}".format(chr(c-32) if islower(str[i]) else chr(c)), end="")
        i = i + 1

    print('')
