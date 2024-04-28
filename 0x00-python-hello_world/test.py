#!/usr/bin/python3
import sys
arg_value = sys.argv
paths = sys.path
print(f"sys.version yields:\n{sys.version}\n")
print(f"sys.platform yields:\n{sys.platform}\n")
for arg_v in arg_value:
    print(f"sys.argv yields:\n{arg_v}\n")
for path_value in paths:
    print(f"sys.path yields:\n{path_value}\n")
