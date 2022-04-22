#!/usr/bin/env python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
r1 = canUnlockAll(boxes)
print(r1 is True)

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
r2 = canUnlockAll(boxes)
print(r2 is True)

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes) is False)

boxes = []
print(canUnlockAll(boxes) is True)

boxes = [[]]
print(canUnlockAll(boxes) is True)

boxes = [[1, 2], [], []]
print(canUnlockAll(boxes) is True)

boxes = [[1, 2, 3, 10], [], [], [], []]
print(canUnlockAll(boxes) is False)

boxes = [[1, 2, 3, 10], [], [], [], []]
print(canUnlockAll(boxes) is False)

boxes = [[1, 2, 3, 10], [], [], [5], []]
print(canUnlockAll(boxes) is False)

boxes = [[2], [1, 2], []]
print(canUnlockAll(boxes) is False)

boxes = [[2], [1, 2], [2]]
print(canUnlockAll(boxes) is False)

boxes = [[2], [1, 2], [2, 1]]
print(canUnlockAll(boxes) is True)
