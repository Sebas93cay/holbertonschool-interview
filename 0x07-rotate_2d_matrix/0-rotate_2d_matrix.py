#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate in place a n x n matrix clock-wise
    """
    matrixCopy = [list.copy(row) for row in matrix]
    n = len(matrix)
    for y in range(n):
        for x in range(n):
            matrix[x][n - 1 - y] = matrixCopy[y][x]
