#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_c = len(argv)
    if arg_c == 1:
        print("{} arguments.".format(arg_c - 1))
    if arg_c == 2:
        print("{} argument:\n1: {}".format(arg_c - 1, argv[1]))
    if arg_c > 2:
        print("{} arguments:".format(arg_c - 1))
        for count in range(1, arg_c):
            print("{}: {}".format(count, argv[count]))
