#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()

print("\n", LockedClass.__dict__)

lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print()
    print("[{}] {}".format(e.__class__.__name__, e))
