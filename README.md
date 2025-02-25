# Sudoku Solver

## Overview

This project is a flexible Sudoku solver that supports different board sizes, including 4x4, 6x6, 9x9, 12x12, and 16x16. It utilizes a backtracking algorithm to find all possible solutions for a given Sudoku puzzle.

## Features

- Supports multiple Sudoku grid sizes (4x4, 6x6, 9x9, 12x12, 16x16)
- Implements a backtracking algorithm to solve puzzles
- Provides a formatted output for better readability
- Modular structure with separate components for solving, validation, and board management

## Installation

Clone this repository:

```bash
git clone https://github.com/HarshKataria12/sudoku-solver.git
```

Navigate to the project directory:

```bash
cd sudoku-solver
```

Ensure you have Python installed (Python 3 recommended).

## Usage

Run the Sudoku solver by executing:

```bash
python main.py
```

The program will attempt to solve all predefined Sudoku grids in `boards.py` and print the solutions.

## Project Structure

```
├── solver.py       # Core backtracking algorithm
├── utils.py        # Utility functions (printing, box size calculation)
├── boards.py       # Predefined Sudoku grids
├── main.py         # Main script to execute the solver
├── README.md       # Project documentation
```

## How It Works

- **Grid Representation**: Sudoku boards are stored in a dictionary format in `boards.py`.
- **Backtracking Algorithm**: The `solve` function in `solver.py` recursively fills empty cells with valid numbers.
- **Validation**: The `possible` function checks if a number can be placed in a given cell without violating Sudoku rules.
- **Output Formatting**: The `print_board` function displays the board in a structured format.

## Example Output

**Initial 9x9 Sudoku Board:**
```
 0  0  7 | 0  0  0 | 0  0  0
 0  0  9 | 2  0  0 | 0  0  4
 ...
```

**1 solution(s) found for 9x9 Sudoku:**
```
 5  3  7 | 6  1  9 | 2  8  4
 6  1  9 | 2  8  4 | 3  5  7
 ...
```

## Customization

To solve a custom Sudoku board, modify `boards.py` and add your puzzle using the same format.

## License

This project is open-source and available under the MIT License.

## Contributions

Contributions are welcome! Feel free to submit pull requests or open issues for improvements and bug fixes.

## Author

Developed by [Harsh Kataria]


