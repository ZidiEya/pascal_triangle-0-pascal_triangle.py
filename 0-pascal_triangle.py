#!/usr/bin/python3
"""
Function that returns Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Sum of two elements directly above
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
