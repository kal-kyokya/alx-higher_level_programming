#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if (char % 2 == 0):
        print(chr(char), end="")
    else:
        print("{}".format(chr(char - 32)), end="")
