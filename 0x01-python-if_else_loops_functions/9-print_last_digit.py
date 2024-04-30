#!/usr/bin/python3
def print_last_digit(number):
    '''This function sends the last digit of an integer input to the standard output.'''
    if number >= 0:
        print("{}".format(number % 10), end="")
        return number % 10
    else:
        print("{}".format((number * -1) % 10), end="")
        return (number * -1) % 10
