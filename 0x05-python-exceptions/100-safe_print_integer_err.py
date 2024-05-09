#!/usr/bin/python3
def safe_print_integer_err(value):
    '''Prints an input value if it is an integer.

    Arg:
        value: Input to be assessed before printing.

    Return:
        True if input is an integer, false otherwise.
    '''
    result = True

    try:
        print("{:d}".format(value))
    except ValueError as err:
        result = False
        print("Exception: {}".format(err))

    return result
