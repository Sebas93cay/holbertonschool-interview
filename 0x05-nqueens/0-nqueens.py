#!/usr/bin/python3
"""
#!/usr/bin/python3
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves the N
queens problem.
"""

from re import I
import sys


def checkAttack(queens):
    """
    check if the there are queens attacking each other in queens
    """
    for i, queen in enumerate(queens):
        if (queen in queens[i + 1:]):
            return True
        for j, secondQueen in enumerate(queens[i + 1:]):
            if (abs(queen-secondQueen) == abs(i-(j + i + 1))):
                return True
    return False


def nextRow(qns, N, sols=[]):
    """
    put a new queen in the next row and continues algorithm from there
    """
    queens = qns.copy()
    nQueens = len(queens)
    if (nQueens == N):
        sols.append(queens)
        return
    for i in range(N):
        queens.append(i)
        if (checkAttack(queens)):
            queens.pop()
        else:
            nextRow(queens, N, sols)
            queens.pop()


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage: nqueens N')
        exit(1)
    arg = sys.argv[1]
    if(not arg.isdigit()):
        print('N must be a number')
        exit(1)
    N = int(arg)
    if (N < 4):
        print('N must be at least 4')
        exit(1)

    solutions = []
    nextRow([], N, solutions)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])
