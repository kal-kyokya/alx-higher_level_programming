#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Only prints the first x integer elements found in a list.

    Args:
        my_list: List to be processed.
        x: The number of elements to be printed.

    Return:
        The total number of integer printed.
    '''
    i = 0
    printed = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            printed += 1
        except (ValueError, TypeError):
            i += 1
            pass

    print()
    return (printed)
