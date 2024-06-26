#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import (add, sub, mul, div)
    import sys
    from sys import argv
    argc = len(argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])
    if sign == '+':
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign == '-':
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign == '*':
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign == '/':
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknow operator. Available operators: +, -; * and /")
        sys.exit(1)
