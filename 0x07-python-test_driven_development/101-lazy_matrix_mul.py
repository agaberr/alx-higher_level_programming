#!/usr/bin/python3
"""
multiply matricies module
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiply 2 matricies using numpy"""
    return numpy.matmul(m_a, m_b)
