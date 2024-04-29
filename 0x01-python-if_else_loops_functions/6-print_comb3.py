#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if ((num1 * 10) + num2) == 89:
            print("{:02d}".format((num1 * 10) + num2))
        elif ((num1 * 10) + num2) < ((num2 * 10) +num1):
            print("{:02d}".format((num1 * 10) + num2), end=", ")
        elif ((num1 * 10) + num2) > ((num2 * 10) +num1):
            continue
        elif ((num1 * 10) + num2) == ((num2 * 10) +num1):
            continue
