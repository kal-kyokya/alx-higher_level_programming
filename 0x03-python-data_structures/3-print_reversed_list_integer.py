#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints a list in reverse order.

    Arg:
        my_list: List to be reversed and printed.

    Return:
        Nothing.
    '''
    len = 0
    for num in my_list:
        len += 1
    for count in range(len - 1, -1, -1):
        print("{:d}".format(my_list[count]))
