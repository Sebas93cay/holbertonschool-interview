#!/usr/bin/python3
"""
This is a interview exercise
This is the second exercise for holberton interviews
"""


def canUnlockAll(boxes, keys=[0], opened=None, key=0):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    canUnlockAll determine if all the boxes can be opened
    """
    if len(keys) >= len(boxes) or len(boxes) == 0:
        return True

    if opened is None:
        opened = []

    if key >= len(boxes):
        return False

    newKeys = boxes[key]
    keys = list(set(keys).union(set(newKeys)))
    opened.append(key)

    for newKey in newKeys:
        if not(newKey in opened) and canUnlockAll(boxes, keys, opened, newKey):
            return True

    return False
