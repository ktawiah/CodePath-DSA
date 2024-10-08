from collections import deque


def has_path(graph, src, dest):
    stack = [src]

    while stack:
        current_node = stack.pop()

        if current_node == dest:
            return True

        for neighbor in graph[current_node]:
            stack.append(neighbor)

    return False


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


def has_path_bft(graph, src, dest):
    queue = deque(src)

    while queue:
        current_node = queue.popleft()

        if current_node == dest:
            return True

        for neighbor in graph[current_node]:
            queue.append(neighbor)

    return False


def has_path_with_edges(edges, src, dest):
    """
    1. Convert edges into graph
    2. Use bfs to find the path
    """
    queue = deque(src)
    visited = set()
    graph = convert_adjacency_to_graph(edges)
    while queue:
        current_node = queue.popleft()

        for neighbor in graph.get(current_node):
            if neighbor == dest:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


def has_path_dfs_with_edges(edges, src, dest):
    pass


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["k"], "j": ["i"], "k": []}
edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
print(has_path(graph, "f", "j"))
print(has_path_bft(graph, "f", "j"))
print(has_path_with_edges(edges, "i", "k"))
