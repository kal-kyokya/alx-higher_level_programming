#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''Sets nth element of a list

    Args:
        my_list: List to be edited.
        idx: Index at which replacement occurs.
        element: Value to be inserted at idx.

    Return:
        my_list whether changes occured or not
    '''
    if idx < 0:
        return my_list
    count = 0
    for num in my_list:
        if count == idx:
            my_list[count] = element
            return my_list
        count += 1
    return my_list
