#!/usr/bin/python3
"""Module for matrix division.

This module provides a function `matrix_divided` that divides all elements
of a matrix by a given divisor, returning a new matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be a non-zero integer or float.

    Returns:
        A new matrix containing the divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)) or elem != elem or elem in (
                    float('inf'), float('-inf')):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div or div in (float('inf'), float('-inf')):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
