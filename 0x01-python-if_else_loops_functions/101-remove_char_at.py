#!/usr/bin/python3
def remove_char_at(str, n):
    '''This function execute a deletion operation in string str at index n.'''
    new_str = ""
    count = 0
    for char in str:
        if (count != n):
            new_str += char
        count += 1
    return new_str
