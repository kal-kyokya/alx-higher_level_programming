#!/usr/bin/python3
for num1 in range(0, 8):
    for num2 in range(0, 10):
        if (num1 == num2):
            continue
        if (num1 >= num2):
            continue
        print("{:d}".format(num1), end="")
        print("{:d}".format(num2), end=", ")
print("89")
