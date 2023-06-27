#!/usr/bin/python3
"""
Defines the Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): size of the square.
        __position (tuple): position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): size of the square. Defaults to 0.
            position (tuple): position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size or position has invalid values.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves size of the square.

        Returns:
            int: size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets size of the square.

        Args:
            value (int): size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves position of the square.

        Returns:
            tuple: position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets position of the square.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: If value is not a tuple or contains invalid values.
            ValueError: If position has invalid values.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) for val in value) or any(val < 0 for val in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns area of the square.

        Returns:
            int: area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints square using the '#' character.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
