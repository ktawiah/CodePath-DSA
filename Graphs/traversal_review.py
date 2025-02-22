def depth_first_traversal(graph, starting_point):
    stack = [starting_point]

    result = [starting_point]
    visited = set()

    while stack:
        node = stack.pop()

        for neighbor in graph.get(node):
            if neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
                stack.append(neighbor)

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
