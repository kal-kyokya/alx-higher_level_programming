#!/usr/bin/python3
def no_c(my_string):
    '''Removes any lowercase and/or uppercase 'c' from a string

    Args:
        my_string: The string to be processed.

    Return:
        The new string version.
    '''
    new_str = ""
    for count in range(0, len(my_string)):
        if my_string[count] == 'c' or my_string[count] == 'C':
            continue
        else:
            new_str = new_str + my_string[count]
    return new_str
