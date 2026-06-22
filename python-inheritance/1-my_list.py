#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """A custom list class that adds functionality to look at sorted elements."""

    def print_sorted(self):
        """Prints the elements of the list sorted in ascending order."""
        print(sorted(self))
        