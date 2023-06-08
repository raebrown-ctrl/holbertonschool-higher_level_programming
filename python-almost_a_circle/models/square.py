#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square instance

        Args:
            size (int): size of the square
            x (int, optional): x position of the square. Defaults to 0.
            y (int, optional): y position of the square. Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size of the square"""
        self.width = self.height = size

    def __str__(self):
        """Method that returns a string representation
        of the Square instance."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.width,  # or self.height
            'x': self.x,
            'y': self.y
        }
