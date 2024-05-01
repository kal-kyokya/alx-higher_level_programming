#!/usr/bin/python3
def multiple_returns(sentence):
    '''Generates length and first character of a string stored in tuple.

    Arg:
        sentence: The string to be processed.

    Return:
        A tuple contain length and first character.
    '''
    if len(sentence) == 0:
        len_and_char = len(sentence), None
    else:
        len_and_char = len(sentence), sentence[0]
    return len_and_char
