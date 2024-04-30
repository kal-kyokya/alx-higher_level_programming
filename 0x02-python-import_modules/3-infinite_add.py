#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_c = len(argv)
    sum = 0
    for count in range(1, arg_c):
        sum += int(argv[count])
    print(f"{sum:d}")
