#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

rec1 = Rectangle(8, 4)
rec2 = Rectangle(2, 3)

print('rec1 Area:', rec1.area(), '\nrec2 Area:', rec2.area())

if rec1 is Rectangle.bigger_or_equal(rec1, rec2):
    print("rec1 is bigger or equal to rec2")
else:
    print("rec2 is bigger than rec1")


rec2.width = 10
rec2.height = 5

print('rec1 Area:', rec1.area(), '\nrec2 Area:', rec2.area())

if rec1 is Rectangle.bigger_or_equal(rec1, rec2):
    print("rec1 is bigger or equal to rec2")
else:
    print("rec2 is bigger than rec1")
