def print_matrix(matrix):
    """
    S: Loop through matrix
    """
    visited = set()
    # stack = []
    # for row in range(len(matrix)):
    #     for col in range(len(matrix[row])):
    #         while col == len(matrix[row]) - 1 or matrix[row][col] in visited:
    #             visited.add(matrix[row][col])
    #             row += 1

    #         visited.add(matrix[row][col])
    #         print(visited, matrix[row][col])

    row = 0
    col = 0

    while row < len(matrix):
        while col < len(matrix[-1]):
            visited.add(matrix[row][col])

            if row + col == len(matrix[-1]):
                while row:
                    print(matrix[row][col])
            col += 1

        col = 0

        row += 1


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print(print_matrix(matrix))

matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
]


print(print_matrix(matrix))
