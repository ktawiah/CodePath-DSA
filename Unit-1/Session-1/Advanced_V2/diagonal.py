"""
Write a function diagonal_sum() that accepts a 2D n x n matrix grid and returns the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements in the secondary diagonal that are not part of the primary diagonal.

The primary diagonal is all cells in the matrix along a line drawn from the top-left cell in the matrix to the bottom-right cell. The secondary diagonal is all cells in the matrix along a line drawn from the top-right cell in the matrix to the bottom-left cell.
"""


def diagonal_sum(grid):
    """
    P: Determine the sum of all the values on the primary and secondary diagonals, without repetition of elements
    """
    # Create a set to store visited cells
    visited = set()

    # Create placeholder to store sum
    diag_sum = 0

    # Create row and col pointers to keep track of secondary diagonal
    sec_row = 0
    sec_col = len(grid[0]) - 1

    # Iterate through matrix and Update sum when current cell not in visited
    for row_idx, row_val in enumerate(grid):
        for col_idx, col_val in enumerate(row_val):
            if (row_idx, col_idx) not in visited and row_idx == col_idx:
                diag_sum += col_val
                visited.add((row_idx, col_idx))

        if (sec_row, sec_col) not in visited and sec_row < len(grid) and sec_col > -1:
            diag_sum += grid[sec_row][sec_col]
            visited.add((sec_row, sec_col))
        sec_row += 1
        sec_col -= 1

    print(diag_sum)


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]  # 25
diagonal_sum(grid)

grid = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]  # 8
diagonal_sum(grid)

grid = [
    [5],
]  # 5
diagonal_sum(grid)
