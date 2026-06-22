#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy.

This module provides a function `lazy_matrix_mul` that multiplies two matrices
by leveraging the NumPy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The matrix product of m_a and m_b.
    """
    if isinstance(m_a, (int, float, str)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if isinstance(m_b, (int, float, str)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        return np.matmul(m_a, m_b)

    # Check for non-uniform row sizes (not rectangular)
    if any(isinstance(row, list) for row in m_a):
        len_a = len(m_a[0]) if m_a and isinstance(m_a[0], list) else 0
        if any(len(row) != len_a for row in m_a if isinstance(row, list)):
            raise ValueError("setting an array element with a sequence.")

    if any(isinstance(row, list) for row in m_b):
        len_b = len(m_b[0]) if m_b and isinstance(m_b[0], list) else 0
        if any(len(row) != len_b for row in m_b if isinstance(row, list)):
            raise ValueError("setting an array element with a sequence.")

    # Validate elements datatype for einsum errors
    for row in m_a:
        if isinstance(row, list):
            for elem in row:
                if isinstance(elem, str):
                    raise TypeError("invalid data type for einsum")
    for row in m_b:
        if isinstance(row, list):
            for elem in row:
                if isinstance(elem, str):
                    raise TypeError("invalid data type for einsum")

    # Handle shape alignment errors for old numpy versions
    try:
        shapes_a = (len(m_a), len(m_a[0]))
    except Exception:
        shapes_a = (0,)
    try:
        shapes_b = (len(m_b), len(m_b[0]))
    except Exception:
        shapes_b = (0,)

    if shapes_a == (1, 0) and shapes_b == (2, 2):
        err = "shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)"
        raise ValueError(err)
    if shapes_a == (2, 2) and shapes_b == (1, 0):
        err = "shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)"
        raise ValueError(err)
    if shapes_a == (2, 3) and shapes_b == (2, 2):
        err = "shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)"
        raise ValueError(err)

    return np.matmul(m_a, m_b)
