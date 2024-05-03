#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''Replaces or adds a key:value pair in a dictionary.

    Args:
        a_dictionary: The dictionary to be processed.
        key: Name of the key to be updated or edited.
        value: Value for updation or addition.

    Return:
        The updated dictionary version.
    '''
    d = a_dictionary
    if key in d:
        d[key] = value
    else:
        d.setdefault(key, value)
    return d
