#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x position of the rectangle. Defaults to 0.
            y (int, optional): y position of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x position of the rectangle"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y position of the rectangle"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Method that returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """
        This method prints the rectangle to
        stdout using the "#" character, taking into
        account the x and y attributes.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Method that returns a string representation
        of the Rectangle instance."""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        This method updates the attributes of the Rectangle instance
        as per the arguments provided."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
