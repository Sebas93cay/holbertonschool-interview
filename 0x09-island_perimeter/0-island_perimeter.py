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
    return perimeter


def findFirstBorder(map):
    """
    Returns the first cells where that contains in between a piece of
    island'b border
    If there is no island returns None
    """
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 1:
                return [(y, x), (1, 0)]
    return None


def roundIslandFromPoint(map, border, end):
    """
    Round whole island starting from start.
    Returns perimeter
    """
    if nextToEndBorder(border, end):
        return 1
    nextBorder = findNextBorder(map, border)
    return roundIslandFromPoint(map, nextBorder, end) + 1


def nextToEndBorder(border, end):
    """
    Checks if start border is next to end border 
    return True if True, False otherwise
    """
    if addVectors(border[0], border[1]) == end[0]:
        return True
    return False


def addVectors(vector1, vector2):
    """
    Return addition of vectors
    """
    return tuple(map(sum, zip(vector1, vector2)))


def findNextBorder(map, border):
    """
    Returns the next border after 'border' following a
    anti-clock-wise rounding to the island
    """
    nextPoint = addVectors(border[0], border[1])
    for direction in posibleDirections(border[1]):
        posible_border = (nextPoint, direction)
        if isBorder(map, posible_border):
            return posible_border
    return None


def posibleDirections(direction):
    """Returns 3 posible directions for next border"""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    reverseDirection = tuple(map(lambda x: -x, direction))
    i = directions.index(reverseDirection)
    return directions[(i + 1):] + directions[:i]


def isBorder(map, posible_border):
    """
    Returns True if posible_border is a border in map
    otherwise returns False
    """
    point = posible_border[0]
    dir = posible_border[1]
    borderCheckerSet = {(0, 1): ((0, 0), (-1, 0)),
                        (0, -1): ((0, -1), (-1, -1)),
                        (1, 0): ((0, 0), (0, -1)),
                        (-1, 0): ((-1, 0), (-1, -1))}
    if (getLand(map, addVectors(point, borderCheckerSet[dir][0])) +
            getLand(map, addVectors(point, borderCheckerSet[dir][1]))) == 1:
        return True
    return False


def getLand(map, point):
    """Returns 1 if point is land in map, 0 otherwise."""
    if (point[0] == -1 or point[1] == -1):
        return 0
    try:
        return map[point[0]][point[1]]
    except IndexError:
        return 0
