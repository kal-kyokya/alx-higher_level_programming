#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    '''Sums all unique elements found in a list.

    Arg:
        my_list: List to be processed.

    Return:
        The sum of all unique numbers in list.
    '''
    return reduce(lambda x, y: x + y, set(my_list))
