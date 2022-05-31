#!/usr/bin/env python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
# validUTF8Mateo = __import__('0-validate_utf8').validUTF8Mateo

# data = [225, 129, 129, 129]
# print(validUTF8(data))

data = [241, 129, 129, 129, 100, 193]
print(validUTF8(data))

# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print(validUTF8(data))

# data = [229, 65, 127, 256]
# print(validUTF8(data))
