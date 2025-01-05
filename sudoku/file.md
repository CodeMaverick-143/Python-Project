# Sudoku Solver

This project is a Python-based program to solve Sudoku puzzles using a backtracking algorithm. The program identifies empty cells, tests valid numbers, and recursively solves the puzzle while ensuring the solution adheres to Sudoku rules. If a solution exists, the program prints the solved puzzle and the time taken to solve it.

---

## Features
- Solves any valid 9x9 Sudoku puzzle.
- Validates numbers against Sudoku rules (row, column, and 3x3 sub-grid constraints).
- Uses backtracking to efficiently explore solutions.
- Provides the time taken to solve the puzzle.

---

## Code Overview

### Functions

1. **`is_valid(board, row, col, num)`**
   - Validates if a number can be placed in a specific cell without breaking Sudoku rules.

   ```python
   def is_valid(board, row, col, num):
       for i in range(9):
           if board[row][i] == num or board[i][col] == num:
               return False

       start_row, start_col = 3 * (row // 3), 3 * (col // 3)
       for i in range(start_row, start_row + 3):
           for j in range(start_col, start_col + 3):
               if board[i][j] == num:
                   return False

       return True
   ```

2. **`solve_sudoku(board)`**
   - Recursively solves the Sudoku puzzle using backtracking.

   ```python
   def solve_sudoku(board):
       for row in range(9):
           for col in range(9):
               if board[row][col] == 0:
                   for num in range(1, 10):
                       if is_valid(board, row, col, num):
                           board[row][col] = num
                           if solve_sudoku(board):
                               return True
                           board[row][col] = 0  # Backtrack
                   return False
       return True
   ```

3. **`print_board(board)`**
   - Formats and prints the Sudoku board.

   ```python
   def print_board(board):
       for row in board:
           print(" ".join(str(num) if num != 0 else '.' for num in row))
   ```

4. **`sudoku_solver(board)`**
   - The main function to solve a Sudoku puzzle and print the result with timing information.

   ```python
   def sudoku_solver(board):
       start_time = time.time()
       if solve_sudoku(board):
           end_time = time.time()
           print("Solved Sudoku Puzzle:")
           print_board(board)
           print(f"Time taken: {end_time - start_time:.4f} seconds")
       else:
           print("No solution exists.")
   ```

---

## Example Usage

The program uses a sample Sudoku puzzle where `0` represents empty cells. Replace the `puzzle` variable with your own puzzle to solve.

### Example Input
```python
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_solver(puzzle)
```

### Output
```plaintext
Solved Sudoku Puzzle:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
Time taken: 0.0012 seconds
```

---

## How It Works
1. The board is represented as a 2D list of integers.
2. The program recursively tries each number from 1 to 9 in empty cells.
3. The `is_valid` function ensures Sudoku rules are followed.
4. If a number works, the program proceeds; otherwise, it backtracks.

---

## Improvements
- Add a GUI for a better user experience.
- Optimize the backtracking algorithm further.
- Implement heuristics like "Most Constrained Variable" to speed up solving.

---

## Dependencies
- Python 3.x
- `time` module (standard library)

---

## Run the Program
Save the code in a file, e.g., `sudoku_solver.py`, and run it:

```bash
python sudoku_solver.py
```

---

Happy solving!
