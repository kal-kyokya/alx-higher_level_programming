#!/usr/bin/python3
Square = __import__('3-square').Square

my_square1 = Square(3)
print("Area: {}".format(my_square1.area()))

try:
    print(my_square1.size)
except AttributeError as err:
    print(err)

try:
    print(my_square1.__size)
except AttributeError as err:
    print(err)

my_square2 = Square(5)
print("Area: {}".format(my_square2.area()))
