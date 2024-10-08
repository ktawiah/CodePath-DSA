from collections import deque


def dfs_iterative(graph, start):
    stack = [start]
    result = [start]
    visited = set()

    while stack:
        current_node = stack.pop()

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                result.append(neighbor)

    return result


def bfs_iterative(graph, start):
    queue = deque(start)
    result = [start]
    visited = set()

    while queue:
        current_node = queue.popleft()

        for neighbor in graph.get(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
                queue.append(neighbor)
    return result


def convert_adjacency_to_graph(a_list):
    graph = {}

    for edge in a_list:
        node1, node2 = edge[0], edge[1]
        if node1 not in graph:
            graph[node1] = []

        if node2 not in graph:
            graph[node2] = []

        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

print(dfs_iterative(graph, "a"))
print(bfs_iterative(graph, "a"))
print(convert_adjacency_to_graph([[1, 2], [2, 3], [4, 5]]))
