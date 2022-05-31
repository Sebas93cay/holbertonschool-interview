#!/usr/bin/python3
"""
This is the exercise 04 of the holberton interviews projects
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    bytes = map(lambda x: format(x & 255, "08b"), data)
    starts = ['10', '0', '110', '1110', '11110']
    limit = 0
    byteCounter = 0
    for ch in bytes:
        if(not any([ch.startswith(code) for code in starts])
           or ch == '00000000'):
            return False
        if (ch.startswith(starts[0])):
            byteCounter = byteCounter + 1
            if (byteCounter > limit):
                return False
        byteCounter = 1
        if (ch.startswith(starts[1])):
            limit = 1
        if (ch.startswith(starts[2])):
            limit = 2
            pass
        if (ch.startswith(starts[3])):
            limit = 3
            pass
        if (ch.startswith(starts[4])):
            limit = 4
            pass
    return True
