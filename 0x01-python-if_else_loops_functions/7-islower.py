#!/usr/bin/python3
def islower(c):
    '''This function checks whether the input is a lowercase character or not.'''
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False
