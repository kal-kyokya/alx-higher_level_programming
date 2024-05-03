#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''Multiplies all elements of a list by a specific input number.

    Args:
        my_list: List to be processed.
        number: Integer by which list gets multiplied.

    Return:
        The new list version.
    '''
    return list(map(lambda x: x * number, my_list))
