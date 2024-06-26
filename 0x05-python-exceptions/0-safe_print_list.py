#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements from a list

    Args:
        my_list: The list containing elements to be printed.
        x: The number of elements requested to be sent to stdout.

    Return: The total number of elements printed.
    '''
    i = 0
    try:
        while i < x:
            print("{}".format(str(my_list[i])), end="")
            i += 1
    except IndexError:
        pass
    print()
    return (i)
