#!/usr/bin/python3
def safe_function(fct, *args):
    '''Executes a function safely.

    Arg:
        fct: The function to be executed.
        args: Tha arguments to the fct function.

    Return:
        The result of the funtion fct or None if an error occured.
    '''
    import sys
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
