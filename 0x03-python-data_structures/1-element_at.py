#!/usr/bin/python3
def element_at(my_list, idx):
    '''Retrieves nth elements of a list.

    Args:
        my_list: The actual list.
        idx: The index at which retrieval occurs.

    Return:
        The nth element or None if failure.
    '''
    if idx < 0:
        return None
    count = 0
    for num in my_list:
        if count == idx:
            return my_list[count]
        count += 1
    return None
