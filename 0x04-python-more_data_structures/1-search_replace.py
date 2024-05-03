#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Creates a list version where all occurences of x are replaced by y.

    Args:
        my_list: List to be processed.
        search: Element to be replaced.
        replace: Replacement for all occurence of 'search'.

    Return:
        The new list version.
    '''
    return [replace if (num == search) else num for num in my_list]
