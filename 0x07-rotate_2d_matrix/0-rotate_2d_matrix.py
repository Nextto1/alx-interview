#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Ritate a 2d square matrix 90 degrees
    Args:
        matrix (list): 2d square
    Return:
        None
    """
    n = len(matrix)
    for k in range(n):
        for j in range(k):
            temp = matrix[k][j]
            matrix[k][j] = matrix[j][k]
            matrix[j][k] = temp

    for k in range(n):
        for j in range(int(n / 2)):
            temp = matrix[k][j]
            matrix[k][j] = matrix[k][n-1-j]
            matrix[k][n-1-j] = temp
