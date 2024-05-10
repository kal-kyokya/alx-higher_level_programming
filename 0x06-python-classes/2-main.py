#!/usr/bin/python3
Square = __import__('2-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

my_square0 = Square()
print(type(my_square0))
print(my_square0.__dict__)

try:
    print(my_square.size)
except AttributeError as err:
    print(err)

try:
    print(my_square.__size)
except AttributeError as err:
    print(err)

try:
    my_square2 = Square("3")
    print(type(my_square2))
    print(my_square2.__dict__)
except TypeError as err:
    print(err)

try:
    my_square3 = Square(-89)
    print(type(my_square3))
    print(my_square3.__dict__)
except ValueError as err:
    print(err)
