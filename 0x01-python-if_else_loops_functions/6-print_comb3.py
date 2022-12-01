#!/usr/bin/python3
n1 = 48
n2 = 49
for i in range(0, 10):
    for j in range(0, 9):
        if n1 >= n2 + j:
            pass
        else:
            print("{}{}".format(chr(n1), chr(n2 + j)), end="")
            if n1 == 56 and j == 8:
                pass
            else:
                print(", ", end="")
    n1 = n1 + 1
print("")
