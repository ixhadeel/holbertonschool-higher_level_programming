#!/usr/bin/python3
"""Module for matrix multiplication.

This module provides a function `matrix_mul` that multiplies two matrices
after strict validation of their dimensions and elements.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a: The first matrix (list of lists of ints/floats).
        m_b: The second matrix (list of lists of ints/floats).

    Raises:
        TypeError: If either matrix is not a list, not a list of lists,
                   contains non-numbers, or has non-uniform row sizes.
        ValueError: If either matrix is empty, or if they cannot be multiplied.

    Returns:
        A new matrix representing the product of m_a and m_b.
    """
    # 1. Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Check if m_a and m_b are empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Check if elements are integers or floats
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Check if all rows in each matrix have the same size (rectangle check)
    m_a_len = len(m_a[0])
    if not all(len(row) == m_a_len for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    m_b_len = len(m_b[0])
    if not all(len(row) == m_b_len for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Check if matrices can be multiplied (cols of m_a == rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7. Perform Matrix Multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row_result.append(total)
        result.append(row_result)

    return result
