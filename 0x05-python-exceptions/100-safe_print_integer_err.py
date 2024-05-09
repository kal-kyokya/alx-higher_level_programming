#!/usr/bin/python3
def safe_print_integer_err(value):
    '''Prints an input value if it is an integer.

    Arg:
        value: Input to be assessed before printing.

    Return:
        True if input is an integer, false otherwise.
    '''
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as err:
        print("Exception: {}".format(err))
        return (False)
