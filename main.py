from solver import solve
from utils import print_board
from boards import grids

def main():
    """Run the Sudoku solver for different board sizes."""
    for size, grid in grids.items():
        print(f"\nInitial {size}x{size} Sudoku Board:")
        print_board(grid)
        
        solutions = []
        solve(grid, size, solutions)
        
        if solutions:
            print(f"\n{len(solutions)} solution(s) found for {size}x{size} Sudoku:")
            for idx, solution in enumerate(solutions, 1):
                print(f"\nSolution {idx}:")
                print_board(solution)
        else:
            print("No solution found.")

if __name__ == "__main__":
    main()
