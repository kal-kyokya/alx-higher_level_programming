#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''Creates a set made of the union of 2 others.

    Args:
        set_1: First set.
        set_2: Second set.

    Return:
        The set containing set_1 U set_2.
    '''
    return set_1 & set_2
