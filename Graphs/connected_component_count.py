def connected_component_count(graph, start):
    stack = [start]
    visited = set()
    count = 0

    while stack:
        current_node = stack.pop()

        for neigbor in graph.get(current_node):
            if neigbor not in visited:
                visited.add(neigbor)
                count += 1
                stack.append(neigbor)

    return count


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

print(connected_component_count(graph, "a"))
