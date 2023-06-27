#!/usr/bin/python3
"""
Defines the Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__check_size(size)
        self.__size = size

    def __check_size(self, size):
        """
        Checks if the provided size is a valid integer.

        Args:
            size (int): size to be checked.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
