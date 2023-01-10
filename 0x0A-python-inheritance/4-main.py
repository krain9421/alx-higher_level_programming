#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if inherits_from(a, float):
    print("{} is an instance of the class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
