#!/usr/bin/python3
"""
This module defines the Square class.
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
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (number): The size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal based on their area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal based on their area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
