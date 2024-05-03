#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Sums all unique elements found in a list.

    Arg:
        my_list: List to be processed.

    Return:
        The sum of all unique numbers in list.
    '''
    sum = 0
    for num in set(my_list):
        sum += num
    return sum
