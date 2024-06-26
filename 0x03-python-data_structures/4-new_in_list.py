#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Makes changes to the copy of list, not the original

    Args:
        my_list: The original list.
        idx: Index at which replacement occurs.
        element: Value tp be inserted at idx.

    Return:
        The new list version, or a copy of the original.
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    count = 0
    for num in my_list:
        if count == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[count])
        count += 1
    return new_list
