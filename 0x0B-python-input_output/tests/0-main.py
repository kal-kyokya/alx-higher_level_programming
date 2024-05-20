#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

print(";-) " * 25, "\n")

read_file("my_file_0.txt")

print(";-) " * 25, "\n")

read_file("0-read_file.py")

print(";-) " * 25, "\n")

try:
    read_file()
except Exception as err:
    print(err)

print(";-) " * 25, "\n")

try:
    read_file("")
except Exception as err:
    print(err)
