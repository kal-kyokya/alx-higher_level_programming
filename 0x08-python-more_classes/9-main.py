#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print(my_square.__dict__)
print("Area: {} - Perimeter: {}".format(
    my_square.area(), my_square.perimeter()))
print(my_square)

square = Rectangle(4, 4)
print(square.__dict__)
print("Area: {} - Perimeter: {}".format(
    square.area(), square.perimeter()))
print(my_square)
