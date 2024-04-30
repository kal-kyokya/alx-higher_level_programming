#!/usr/bin/python3
def uppercase(str):
    '''This function converts all lowercase characters inside a string to upper.'''
    for char in str:
        if ord(char) in range(ord('a'), ord('z') + 1):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
