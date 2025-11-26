#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size  # will use the setter for validation

    @property
    def size(self):
        """Retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
