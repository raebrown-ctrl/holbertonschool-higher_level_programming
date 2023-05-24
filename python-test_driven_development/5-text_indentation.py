#!/usr/bin/python3
""" 4. Text indentation - 5-text_indentation.py """


def text_indentation(text):
    """
    This function prints a text w/ 2 new lines\
        after each: '.' '?' or ':'

    Args:
        text: text to use

    Raises:
        TypeError if text not a string

    Return:
        No return only print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = True

    for char in text:
        if char != ' ' or new_line is False:
            print(char, end='')
            new_line = False
        elif char != ' ':
            new_line = False

        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
