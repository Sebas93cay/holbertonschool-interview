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
    prime_numbers = get_prime_numbers(max(nums))
    for i in range(x):
        counts[game(nums[i], prime_numbers)] += 1
    return getWinner(counts)


def get_prime_numbers(max):
    """Get the prime numbers that are less than max"""
    primes = []
    for i in range(2, max+1):
        if isPrime(i):
            primes.append(i)
    return primes


def game(n, prime_numbers):
    """Simulate a game for n as the length of the array"""
    prime_counter = 0
    for i in prime_numbers:
        if i <= n:
            prime_counter += 1
        else:
            break
    if prime_counter % 2 == 0:
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
