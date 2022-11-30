#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        m3 = i % 3
        m5 = i % 5
        if m3 == 0 and m5 != 0:
            print("Fizz", end=" ")
        elif m5 == 0 and m3 != 0:
            if i == 100:
                print("Buzz", end=" \n")
            else:
                print("Buzz", end=" ")
        elif m5 == 0 and m3 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
