#!/usr/bin/python3
def safe_print_integer_err(value):
    '''Prints an input value if it is an integer.

    Arg:
        value: Input to be assessed before printing.

    Return:
        True if input is an integer, false otherwise.
    '''
    try:
        print("{:d}".format(int(value)))
        return (True)
    except ValueError as err:
        print("Exception:", err)
        return (False)
