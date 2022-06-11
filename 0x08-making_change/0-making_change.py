#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given 
amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given 
    amount total.
    """
    if total <= 0:
        return 0
    if not orderedCoins(coins):
        coins.sort()
    for coinIndex in reversed(range(len(coins))):
        biggerCoinN = int(total / coins[coinIndex])
        if (total % coins[coinIndex] == 0):
            return biggerCoinN
        if (biggerCoinN > 0):
            totalSoFar = coins[coinIndex] * biggerCoinN
            restCoinsN = makeChange(coins[:coinIndex], total - totalSoFar)
            if restCoinsN != -1:
                return restCoinsN + biggerCoinN
    return -1


def orderedCoins(coins):
    """
    return True if list of coins is ordered
    """
    for i in range(len(coins)-1):
        if coins[i] > coins[i + 1]:
            return False
    return True
