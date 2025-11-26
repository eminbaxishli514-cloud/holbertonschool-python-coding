#!/usr/bin/python3
"""This module defines a Square class with validated size."""


class Square:
    """A class that defines a square by its private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with validated size.

        Args:
            size (int): size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
