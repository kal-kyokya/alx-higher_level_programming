#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Only prints the first x integer elements found in a list.

    Args:
        my_list: List to be processed.
        x: The number of elements to be printed.

    Return:
        The total number of integer printed.
    '''
    count = 0

    for x in range(0, x):
        try:
            print("{:d}".format(my_list[x]), end="")
        except IndexError:
            break
        except ValueError:
            pass
        except Exception:
            pass
        else:
            count += 1

    print()
    return count
