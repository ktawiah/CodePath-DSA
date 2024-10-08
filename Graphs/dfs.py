def depth_first_traversal(graph, starting_point):
    """
    1. Keep track of current_node, visited_nodes, result_nodes, stack
    2. Create a stack with starting_point
    3. While stack is not empty:
      - Update current
      - Check if not visited
        - Update visited
        - Update result_list
        - Update stack
    4. Return result

    """
    stack = [starting_point]

    result = []

    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            result.append(current_node)

            neighbors = graph.get(current_node)

            for index in range(len(neighbors) - 1, -1, -1):
                stack.append(neighbors[index])

    return result


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

print(depth_first_traversal(graph, "a"))
