#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only
two operations in this file: Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to result in exactly n H
characters in the file.
"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute only
    two operations in this file: Copy All and Paste. Given a number n, write a method
    that calculates the fewest number of operations needed to result in exactly n H
    characters in the file.
    """
    if n <= 1:
        return 0
    return sum(getFactors(n))


def getFactors(n):
    """
    Return a list with the prime factor of a number
    """
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors
