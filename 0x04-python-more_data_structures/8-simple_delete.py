#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''Deletes a specific key:value pair.

    Args:
       a_dictionary: The dictionary to be edited.
       key: The key name reference the pair to be deleted.

    Return:
        The updated dictionary version.
    '''
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
