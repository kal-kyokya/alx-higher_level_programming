#!/usr/bin/python3
def safe_print_division(a, b):
    '''Divides 2 integers and prints the result.

    Arg:
        a: Dividend
        b: Divisor

    Return:
        The value of the division
    '''
    result = 0

    try:
        result =  a / b
        return result
    except ZeroDivisionError:
        result = None
    finally:
        print("Inisde result: {}".format(result))
