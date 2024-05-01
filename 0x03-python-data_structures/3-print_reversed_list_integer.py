#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints a list in reverse order.

    Arg:
        my_list: List to be reversed and printed.

    Return:
        Nothing.
    '''
    for count in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[count]))
