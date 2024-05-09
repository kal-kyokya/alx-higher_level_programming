#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''Divides element by element 2 lists.

    Args:
        my_list_1: Dividend list
        my_list_2: Divisor list
        list_length: Requested number of division.

    Return:
        A list of length 'list_length' containing the result of division.
    '''
    new_list = []
    i = 0
    result = None

    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("wrong type")
                result = 0
            except (ZeroDivisionError):
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                new_list.append(result)
    finally:
        return (new_list)
