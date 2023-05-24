#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer
if width is less than 0, raise a ValueError
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer
if height is less than 0, raise a ValueError
Instantiation = def __init__(self, width=0, height=0):
def area(self): that returns the rectangle area
def perimeter(self): that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialization method for the Rectangle class

        Attributes:
            width: Width of rectangle
            height: Height of rectangle
        self.width = width
        self.height = height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width: Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width: Width of rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height: height of rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width > 0 and self.height > 0:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0
