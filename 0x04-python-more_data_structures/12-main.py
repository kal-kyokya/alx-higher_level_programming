#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")
roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "CMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "CMXCI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "CMIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")

roman_number = "CMI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print("-----------------")
