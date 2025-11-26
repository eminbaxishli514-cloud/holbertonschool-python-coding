#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """
    A class representing a square.

    Attributes:
        size (int): Length of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
