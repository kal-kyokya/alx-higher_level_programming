#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Converts a roman numeral to an integer.

    Arg:
        roman_string: String denoting the romann numeral.

    Return:
        The integer equivalent of the roman.
    '''
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev_value = 0
    print(f"sum {sum}")

    for char in roman_string:
        current_value = r[char]
        print(f"current {current_value}")
        print(f"prev_value {prev_value}")
        if current_value > prev_value:
            sum += current_value - 2 * prev_value
            print(f"sum1 {sum}")
        else:
            sum += current_value
            print(f"sum2 {sum}")
        prev_value = current_value
    return sum
