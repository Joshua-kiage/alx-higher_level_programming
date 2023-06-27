#!/usr/bin/python3
"""
This module defines the MagicClass class.
"""

import math


class MagicClass:
    """
    Represents a magic class.

    Attributes:
        __radius (int or float): The radius of the magic class.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.

        Args:
            radius (int or float): The radius of the magic class. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic class.

        Returns:
            float: The area of the magic class.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic class.

        Returns:
            float: The circumference of the magic class.
        """
        return 2 * math.pi * self.__radius
