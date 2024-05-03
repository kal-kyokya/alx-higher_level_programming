#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Prints a dictionary's 'key:value' pairs, key's alphabetic order-wise.

    Arg:
        a_dictionary: The dictionary to be processed.

    Return:
        Nothing.
    '''
    d = a_dictionary
    key_list = [keyz for keyz in d.keys()]
    key_list.sort()
    for k in key_list:
        print("{}: {}".format(k, d[k]))
