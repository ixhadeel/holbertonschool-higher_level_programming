#!/usr/bin/python3
"""Module for printing names.

This module provides a function `say_my_name` that takes a first name
and an optional last name and prints them formatted.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The first name string.
        last_name: The last name string (defaults to empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
