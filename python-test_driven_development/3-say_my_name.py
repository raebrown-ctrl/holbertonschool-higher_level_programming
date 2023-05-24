#!/usr/bin/python3
""" 2. Say my name - 3-say_my_name.py """


def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is <first name> <last name>"

    Args:
        first_name: persons first name
        last_name: the last name which defaults to ""

    Raises:
        TypeError if both aren't strings

    Return:
        No return only print
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
