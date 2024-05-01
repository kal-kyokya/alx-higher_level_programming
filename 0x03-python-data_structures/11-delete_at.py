#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''Deletes the nth element of a list.

    Args:
        my_list: The list to be processed.
        idx: Index at which deletion occurs.

    Return:
        An edited my_list if change occured, my_list if not.
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list = my_list[0:idx] + my_list[idx + 1:]
    return my_list
