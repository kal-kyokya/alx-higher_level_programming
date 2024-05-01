#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Finds all multiple of inside a list.

    Arg:
        my_list: The list to be processed.

    Return:
        A list made of matching True and False.
    '''
    new_list = []
    for count in range(0, len(my_list)):
        if my_list[count] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
