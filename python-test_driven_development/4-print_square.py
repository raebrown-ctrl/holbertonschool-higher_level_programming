#!/usr/bin/python3
""" 3. Print square - 4-print_square.py """


def print_square(size):
    """
    This function prints a square with #

    Args:
        size: size of square

    Raises:
        TypeError if size not int
        ValueError if size < 0
        TypeError if size < 0 and is float

    Return:
        No return only print
    """
    if type(size) is not int:
        if type(size) is float and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
