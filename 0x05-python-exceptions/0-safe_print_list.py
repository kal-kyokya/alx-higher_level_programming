#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements from a list

    Args:
        my_list: The list containing elements to be printed.
        x: The number of elements requested to be sent to stdout.

    Return: The actual number of elements printed.
    '''
    try:
        for count in range(0, x):
            print(f"{my_list[count]}", end="")
        print()
        return count + 1
    except Exception:
        count -= 1
        print()
        return count + 1
