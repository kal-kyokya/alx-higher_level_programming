#!/usr/bin/python3
def safe_print_integer(value):
    '''Prints an input value if it is an integer.

    Arg:
        value: The input to be assessed before printing.

    Return:
        True if the input is an integer, false otherwise.
    '''
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
