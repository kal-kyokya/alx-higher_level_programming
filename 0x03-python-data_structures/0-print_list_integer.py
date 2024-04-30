#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''
    This function send elements of a list to stdout one by one, each on a new line

    my_list: The list of elements to be sent to stdout

    Return: Nothing.
    '''
    for num in my_list:
        print("{}".format(num))
    
