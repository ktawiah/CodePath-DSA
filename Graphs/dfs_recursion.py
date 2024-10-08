def dfs_recursion(graph, start):
    result = []

    def helper(graph, start, result):
        result.append(start)

        for neighbor in graph[start]:
            helper(graph, neighbor, result)

    helper(graph, start, result)
    return result
    # if result is None:
    #     result = []

    # result.append(start)

    # if len(result) == len(graph.keys()):
    #     return result

    # for neighbor in graph[start]:
    #     dfs_recursion(graph, neighbor, result)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

print(dfs_recursion(graph, "a"))
