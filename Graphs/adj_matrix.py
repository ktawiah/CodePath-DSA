def min_edges_to_connect(adj_matrix):
    n = len(adj_matrix)  # Number of vertices
    adj_list = {
        i: [] for i in range(n)
    }  # Initialize empty adjacency list for each vertex

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:  # If there's an edge between i and j
                adj_list[i].append(j)  # Add j to the list of i

    return adj_list

    print(adj_list)

    # count = 0
    # visited = set()

    # for row_idx in range(len(adj_matrix)):
    #     for col_idx in range(len(adj_matrix[row_idx])):
    #         if (row_idx, col_idx) not in visited or (col_idx, row_idx) not in visited:
    #             if (
    #                 adj_matrix[row_idx][col_idx]
    #                 == 1
    #                 != adj_matrix[col_idx][row_idx]
    #                 == 0
    #             ):
    #                 count += 1
    #                 visited.add((row_idx, col_idx))
    #                 visited.add((col_idx, row_idx))

    # return count


print(
    min_edges_to_connect(
        [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
    )
)
