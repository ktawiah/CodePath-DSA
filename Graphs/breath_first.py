from collections import deque


def bfs(graph, starting_point):
    queue = deque(starting_point)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

    return result

    # queue = deque(starting_point)  # Queue initialized with the starting point
    # visited = set(starting_point)  # Mark the starting node as visited
    # result_list = [starting_point]  # Initialize result list with the starting point

    # while queue:
    #     current_node = queue.popleft()  # Dequeue the front node

    #     # Visit all the unvisited neighbors
    #     for neighbor in graph[current_node]:
    #         if neighbor not in visited:
    #             visited.add(neighbor)  # Mark neighbor as visited
    #             queue.append(neighbor)  # Enqueue the neighbor
    #             result_list.append(neighbor)  # Add neighbor to the result list

    # return result_list


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

graph2 = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": [],
    "f": [],
    "g": [],
}

print(bfs(graph, "a"))
print(bfs(graph2, "a"))
