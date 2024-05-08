#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Converts a roman numeral to an integer.

    Arg:
        roman_string: String denoting the romann numeral.

    Return:
        The integer equivalent of the roman.
    '''
    r = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    int_values = [1, 5, 10, 50, 100, 500, 1000]
    counter = len(roman_string)
    if counter == 1:
        return int_values[r.index(roman_string)]
    count = 0
    sum = 0
    idx = 0
    for current in roman_string:
        print(f"current is {current}")
        counter -= 1
        if count == 0:
            prev = current
            print(f"prev is {prev}")
            count = 1
            idx += 1
            continue
        if r[idx + 1] == current == r[idx + 2]:
            sum += int_values[idx] - int_values[idx]
            print(f"sum1 is {sum}")
            if counter > 1:
                count = 0
        else:
            sum += int_values[idx] + int_values[idx]
            print(f"sum2 is {sum}")
        print(f"r_idx_prev {r.index(prev)}")
        idx += 1
    return sum
