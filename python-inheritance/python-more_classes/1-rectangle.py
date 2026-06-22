#!/usr/bin/python3
"""Module for defining a Rectangle class.

This module provides a class representation of a geometric rectangle,
utilizing property getters and setters with strict integer type validation.
"""


class Rectangle:
    """A class that defines a rectangle geometric shape."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width length of the rectangle.
            height (int): The height length of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the private width attribute of the rectangle.

        Returns:
            int: The width length of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute of the rectangle with validation.

        Args:
            value (int): The new width length to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the private height attribute of the rectangle.

        Returns:
            int: The height length of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute of the rectangle with validation.

        Args:
            value (int): The new height length to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
