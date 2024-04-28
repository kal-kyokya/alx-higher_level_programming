#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    num = -1
    for char in str:
        num = num + 1
        if (n == num):
            continue
        else:
            result = result + char
    return (result)
