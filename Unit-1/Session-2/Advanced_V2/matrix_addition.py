"""
Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.
"""


def add_matrices(matrix1, matrix2):
    # Loop through one matrix
    # Replace cell by sum of values in that matrix and the other

    for row_idx, row_val in enumerate(matrix1):
        for col_idx, col_val in enumerate(row_val):
            matrix1[row_idx][col_idx] = col_val + matrix2[row_idx][col_idx]

    print(matrix1)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

add_matrices(matrix1, matrix2)
