#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()

print("\n", LockedClass.__dict__)

lc.first_name = "John"
print("\n", lc.first_name)
print("\n", LockedClass.__dict__)

try:
    lc.last_name = "Snow"
except Exception as e:
    print()
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    del lc.first_name
except Exception as err:
    print(err)

try:
    print(lc.first_name)
except Exception as err:
    print(err)
