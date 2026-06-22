#!/usr/bin/python3
"""Module for text indentation.

This module provides a function `text_indentation` that formats text
by adding two newlines after specific characters (., ?, and :).
"""


def text_indentation(text):
    """Prints text with 2 newlines after each '.', '?', and ':'.

    Also ensures that there are no leading or trailing spaces on each line.

    Args:
        text: The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
