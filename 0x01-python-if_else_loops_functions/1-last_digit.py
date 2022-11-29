#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    last = (number * -1) % 10
else:
    last = number % 10

if last > 5:
    text = 'and is greater than 5'
elif last < 6 and last != 0:
    text = 'and is less than 6 and not 0'
else:
    text = 'and is 0'

print('Last digit of', number, 'is', last, text)
