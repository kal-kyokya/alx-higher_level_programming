#!/usr/bin/python
def pow(a, b):
    negative = 0
    if (b == 1):
        return (a)
    elif (b == 0):
        return (1)
    elif (b < 0):
        negative = 1
        b = b * (-1)
    result = a
    while (b != 1):
        result *= a
        b = b - 1
    if (negative == 1):
        result = (1 / result)
    return (result)
