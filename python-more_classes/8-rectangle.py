#!/usr/bin/python3
"""Module for defining a Rectangle class.

This module provides a class representation of a geometric rectangle,
including properties, area/perimeter calculations, and a static method
to compare rectangles based on their calculated areas.
"""


class Rectangle:
    """A class that defines a rectangle geometric shape.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width length of the rectangle.
            height (int): The height length of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate and return the current rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the current rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol.

        Returns:
            str: An empty string if width or height is 0, otherwise
                 the text-based representation of the rectangle shape.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for _ in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """Return a string representation that allows recreating the instance.

        Returns:
            str: A canonical representation string of the Rectangle instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two Rectangle instances based on their area.

        Args:
            rect_1 (Rectangle): The first rectangle instance to compare.
            rect_2 (Rectangle): The second rectangle instance to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle instance.

        Returns:
            Rectangle: The instance with the larger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
