#!/usr/bin/python3
def main():
    import sys
    sum = 0
    num = len(sys.argv)
    if num > 1:
        for i in range(1, num):
            sum = sum + int(sys.argv[i])

    else:
        pass

    print(sum)


if __name__ == "__main__":
    main()
