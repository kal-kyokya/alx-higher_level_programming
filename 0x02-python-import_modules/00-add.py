#!/usr/bin/python3
sum = __import__('add_0').add
print(__name__)
a = 1
b = 2
print("{} + {} = {}".format(a, b, sum(a, b)))
