from utils import get_box_size  # Only import needed utility function
from boards import grids

def possible(grid, row, col, num, size):
    """Check if a number can be placed in a given cell without violating Sudoku rules."""
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(size)]:
        return False
    
    box_rows, box_cols = get_box_size(size)
    x0 = (col // box_cols) * box_cols
    y0 = (row // box_rows) * box_rows
    
    for i in range(box_rows):
        for j in range(box_cols):
            if grid[y0 + i][x0 + j] == num:
                return False
    
    return True

def solve(grid, size, solutions):
    """Find all solutions for the Sudoku board using backtracking."""
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                for num in range(1, size + 1):
                    if possible(grid, row, col, num, size):
                        grid[row][col] = num
                        solve(grid, size, solutions)
                        grid[row][col] = 0
                return
    solutions.append([row[:] for row in grid])

    return True