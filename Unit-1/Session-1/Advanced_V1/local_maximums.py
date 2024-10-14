"""
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.


"""


def local_maximums(grid):
    # Create placeholder for local maxes
    local_maxes = []

    # Iterate through each possible 3x3 matrix
    for row in range(len(grid) - 2):
        # Create a subrow
        sub_row = []
        for col in range(len(grid) - 2):
            # Extract 3x3 matrix
            sub_matrix = [
                grid[row][col],
                grid[row][col + 1],
                grid[row][col + 2],
                grid[row + 1][col],
                grid[row + 1][col + 1],
                grid[row + 1][col + 2],
                grid[row + 2][col],
                grid[row + 2][col + 1],
                grid[row + 2][col + 2],
            ]
            # Find max of extracted matrix
            max_of_sub = max(sub_matrix)
            sub_row.append(max_of_sub)

        # Store in rows of submatrix and add to local matrix
        local_maxes.append(sub_row)
    # Return local matrix
    print(local_maxes)


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
local_maximums(grid)

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]
local_maximums(grid)
