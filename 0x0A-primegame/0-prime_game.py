#!/usr/bin/python3
"""Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game."""

maria = 'Maria'
ben = 'Ben'


def isWinner(x, nums):
    """Return name of the winner"""
    if x > len(nums):
        return None
    counts = {maria: 0, ben: 0}
    for i in range(x):
        counts[game(nums[i])] += 1
        print(counts)
    return getWinner(counts)


def game(n):
    """Simulate a game for n as the length of the array"""
    primeCounter = 0
    numbers = list(range(n + 1))
    for i in numbers[2:]:
        if isPrime(i):
            primeCounter += 1
    if primeCounter % 2 == 0:
        return ben
    return maria


def getWinner(counts):
    """Returns the winner according to the number of wins in counts"""
    if counts[ben] > counts[maria]:
        return ben
    if counts[ben] < counts[maria]:
        return maria
    return None


def isPrime(n):
    """Returns True if the given number is prime"""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, n // 2, 6):
        if n % i == 0:
            return False
    return True
