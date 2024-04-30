#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''Prints list elements, each on a new line

    Arg:
        my_list: The list of elements to be sent to stdout

    Return:
        Nothing.
    '''
    for num in my_list:
        print("{}".format(num))
