#!/usr/bin/python3
def main():
    import hidden_4, sys
    list = dir(hidden_4)
    list.sort()
    for c in list:
        if c[0] == "_" and c[1] == "_":
            pass
        else:
            print(c)


if __name__ == "__main__":
    main()
