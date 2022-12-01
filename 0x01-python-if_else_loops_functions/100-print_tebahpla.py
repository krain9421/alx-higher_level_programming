#!/usr/bin/python3
for c in range(122, 96, -1):
    i = c % 2
    print("{}".format(chr(c-32) if i != 0 else (chr(c))), end="")
