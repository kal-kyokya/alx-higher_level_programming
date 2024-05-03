#!/usr/bin/python3
def best_score(a_dictionary):
    '''Tells which key has the biggest integer value.

    Arg:
        a_dictionary: Dictionary to be processed.

    Return:
        The key name with the biggest value, None otherwise.
    '''
    d = a_dictionary
    if d == None:
        return None
    biggest = 0
    for num in d.values():
        if num >= biggest:
            biggest = num
    for key in d.keys():
        if d[key] == biggest:
            return key
