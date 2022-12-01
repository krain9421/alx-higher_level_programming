#!/usr/bin/python3
def main():
    import sys
    num = len(sys.argv)
    if num <= 1:
        print("0 arguments.")
    else:
        if num <= 2:
            print("1 argument:\n1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(num-1))
            for i in range(1, num):
                print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
