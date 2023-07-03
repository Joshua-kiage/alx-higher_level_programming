#!/usr/bin/python3

"""
N-Queens Problem Solver
"""

import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position on the board.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    """
    Recursively solve the N-Queens problem.
    """
    n = len(board)

    # Base case: All queens have been placed
    if row == n:
        solution = []
        for i in range(n):
            queen_col = board[i].index(1)
            solution.append([i, queen_col])
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0  # Remove the queen


def print_solutions(n, solutions):
    """
    Print the solutions to the N-Queens problem.
    """
    for solution in solutions:
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(solution[i][0], solution[i][1]), end="")
            if i != n - 1:
                print(", ", end="")
        print("]")


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N-Queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    print_solutions(n, solutions)
