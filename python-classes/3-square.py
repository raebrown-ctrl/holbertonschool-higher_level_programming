#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with a message
if size is less than 0, raise a ValueError exception with a message
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module
"""


class Square():
    """This class defines a square with it's size initialized"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.__area = self.__size ** 2
        return self.__area
