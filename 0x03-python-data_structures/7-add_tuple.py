#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''Sums two tuples of 2 elements each..

    Args:
        tuple_a: First tuple.
        tuple_b: Second tuple.

    Return:
        A tuple with 2 elements.
    '''
    if len(tuple_a) < 2:
        list_a = list(tuple_a)
        for count in range(0, 2):
            if count >= len(tuple_a):
                list_a.append(0)
        tuple_a = tuple(list_a)
    if len(tuple_b) < 2:
        list_b = list(tuple_b)
        for count in range(0, 2):
            if count >= len(tuple_b):
                list_b.append(0)
        tuple_b = tuple(list_b)
    tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_c
