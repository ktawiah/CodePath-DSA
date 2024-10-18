"""
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
"""


def transpose(matrix):
    rect_matrix = []
    square_matrix = []

    for size in range(len(matrix[0])):
        rect_matrix.append([0] * len(matrix))

    for size in range(len(matrix)):
        square_matrix.append([0] * len(matrix[0]))

    for row_idx, row_val in enumerate(matrix):
        for col_idx, col_val in enumerate(row_val):
            if len(matrix) == len(matrix[0]):
                # matrix[row_idx][col_idx], matrix[col_idx][row_idx] = (
                #     matrix[col_idx][row_idx],
                #     matrix[row_idx][col_idx],
                # )
                square_matrix[col_idx][row_idx] = matrix[row_idx][col_idx]

            if len(matrix) != len(matrix[0]):
                rect_matrix[col_idx][row_idx] = matrix[row_idx][col_idx]
    return square_matrix if len(matrix) == len(matrix[0]) else rect_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))
