#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(25, 21, 30, 49, 5007)
    print(r1)

    r1.update(height=67)
    print(r1)

    r1.update(56, 84, x=3, y=704, id=179)
    print(r1)

    r1.update(width=19, x=52)
    print(r1)

    r1.update(y=37, width=671, x=23, id=89)
    print(r1)

    r1.update(x=95, height=716, y=853, width=457)
    print(r1)
