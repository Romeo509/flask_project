#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, col, N, solutions):
    """ Recursive function to solve N Queens problem """
    if col >= N:
        # Base case: If all queens are placed, add current solution to solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    
    # Try placing queen in each row of current column
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            solve_nqueens(board, col + 1, N, solutions)  # Recur to place rest of queens
            
            # Backtrack: If placing queen doesn't lead to a solution, remove it
            board[i][col] = 0
    
    return False

def print_solutions(solutions):
    """ Print all solutions """
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Initialize the board as an NxN grid with all cells as 0 (empty)
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    
    # Solve the N Queens problem
    solve_nqueens(board, 0, N, solutions)
    
    # Print all solutions
    print_solutions(solutions)
