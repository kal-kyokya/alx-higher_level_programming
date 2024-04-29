#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    count = 0
    for char in str:
        if (count != n):
            new_str += char
        count += 1
    return new_str
