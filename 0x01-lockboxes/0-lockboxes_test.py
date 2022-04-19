#!/usr/bin/env python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# boxes = [[1], [2], [3], [4], []]
# r1 = canUnlockAll(boxes)
# print(r1)

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# r2 = canUnlockAll(boxes)
# print(r2)

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))

boxes = [[],[]]
print(canUnlockAll(boxes))