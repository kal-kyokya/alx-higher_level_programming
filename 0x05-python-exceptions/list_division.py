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
    result_list = []

    for count in range(0, list_length):
        error = 0
        try:
            result_list.append(0)
            result_list[count] = my_list_1[count] / my_list_2[count]
        except IndexError:
            error = 1
        except ZeroDivisionError:
            error = 2
        except (TypeError, ValueError):
            error = 3
        finally:
            if error == 1:
                print("out of range")
            elif error == 2:
                print("division by 0")
            elif error == 3:
                print("Wrong type")

    return result_list
