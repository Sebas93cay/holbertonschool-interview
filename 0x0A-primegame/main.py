#!/usr/bin/env python

isWinner = __import__('0-prime_game').isWinner
isPrime = __import__('0-prime_game').isPrime


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(2, [3, 5])))
