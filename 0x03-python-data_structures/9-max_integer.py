#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Returns the biggest number found in a list.

    Arg:
        my_list: The list to be processed.

    Return:
        The largest integer found inside my_list.
    '''
    if len(my_list) == 0:
        return None
    new_list = sorted(my_list)
    return new_list[-1]
