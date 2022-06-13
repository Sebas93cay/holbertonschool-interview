#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the perimeter
of the island described in grid:
grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn't have “lakes” (water inside that isn't connected to the
water surrounding the island).
"""


def island_perimeter(map):
    """
    Returns the perimeter of the island
    """
    first_border = findFirstBorder(map)
    if first_border is None:
        return 0
    perimeter = roundIslandFromPoint(map, first_border, first_border)
    return 3


def findFirstBorder(map):
    """
    Returns the first cells where that contains in between a piece of
    island'b border
    If there is no island returns None
    """
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 1:
                return [[y, x], [y, x - 1]]
    return None


def roundIslandFromPoint(map, border, end):
    """
    Round whole island starting from start.
    Returns perimeter
    """
    if nextToEndBorder(border, end):
        return 1
    nextBorder = findNextBorder(map, border)


def nextToEndBorder(border, end):
    """
    Checks if start border is next to end border 
    return True if True, False otherwise
    """
    if border[0] == end[0] and border[1][0] == end[1][0] - 1 and (
            border[1][1] == end[1][1] + 1):
        return True
    return False


def findNextBorder(map, border):
    """
    Returns the next border after 'border' following a
    anti-clock-wise rounding to the island
    """
