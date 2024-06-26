#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Multiply all dictionary values by 2.

    Arg:
       a_dictionary: The dictionary to be processed.

    Return:
        The new dictionary version.
    '''
    d = a_dictionary
    keyz = d.keys()
    new_values = [num * 2 for num in d.values()]
    return dict(zip(keyz, new_values))
