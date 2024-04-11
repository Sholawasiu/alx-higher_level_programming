#!/usr/bin/python3

"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices.

    Args:
        m_a (list of lists of ints/floats): 1st matrix.
        m_b (list of lists of ints/floats): 2nd matrix.

    Returns:
        The Matrix Product
    """
    return np.matmul(m_a, m_b)
