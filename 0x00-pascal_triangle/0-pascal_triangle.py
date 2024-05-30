#!/usr/bin/python3
"""Pascal Triangle Interview Challenge for Alx project by Ernest"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for r in range(n):
        row = [0] * (r+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for k in range(1, r):
            if k > 0 and k < len(row):
                x = pascal_triangle[r - 1][k]
                y = pascal_triangle[r - 1][k - 1]
                row[k] = x + y

        pascal_triangle[r] = row

    return pascal_triangle
