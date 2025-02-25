def get_box_size(size):
    """Return the number of rows and columns per box for different Sudoku sizes."""
    if size == 9:
        return 3, 3
    elif size == 12:
        return 3, 4
    elif size == 16:
        return 4, 4
    elif size == 6:
        return 2, 3
    elif size == 4:
        return 2, 2
    else:
        raise ValueError("Unsupported Sudoku size")

def print_board(grid):
    """Print the Sudoku board with proper formatting."""
    size = len(grid)
    box_rows, box_cols = get_box_size(size)

    for i, row in enumerate(grid):
        if i % box_rows == 0 and i != 0:
            print("-" * (4 * size - 1))  # Horizontal separator

        for j, num in enumerate(row):
            if j % box_cols == 0 and j != 0:
                print("| ", end="")  # Vertical separator
            print(f"{num:2} ", end="")  # Format spacing
        print()
