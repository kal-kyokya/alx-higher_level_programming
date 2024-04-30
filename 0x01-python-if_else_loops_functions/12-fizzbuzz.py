#!/usr/bin/python3
def fizzbuzz():
    '''
    This function prints a specific input based on whether the number is:
    _ A product of (3 and 5)
    _ A product of 3
    _ A product of 5
    _ None of the above
    '''
    for count in range(1, 101):
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz", end=" ")
        elif count % 3 == 0:
            print("Fizz", end=" ")
        elif count % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(count), end=" ")
