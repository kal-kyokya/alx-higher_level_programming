#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Creates a set containing all elements present in only one of the 2 sets.

    Args:
        set_1: First set.
        set_2: Second set.

    Return:
        The set containing (set(set_1 + set_2) - (set_1 U set_2))
    '''
    return set_1 ^ set_2
