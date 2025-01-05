import time

def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively try to solve
                            return True
                        board[row][col] = 0  # Backtrack if invalid
                return False  # No valid number found, backtrack
    return True  # Puzzle solved

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def sudoku_solver(board):
    start_time = time.time()
    if solve_sudoku(board):
        end_time = time.time()
        print("Solved Sudoku Puzzle:")
        print_board(board)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("No solution exists.")
