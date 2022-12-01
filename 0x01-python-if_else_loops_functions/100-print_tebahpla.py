#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 != 0:
        print(chr(c-32), end="")
    else:
        print(chr(c), end="")
