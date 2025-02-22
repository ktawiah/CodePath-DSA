def get_combinations(lst):
    result = []
    stack = [([], 0)]  # Initialize the stack with the starting index and empty path

    while stack:
        path, start = stack.pop()
        result.append(path)

        # Iterate through the remaining elements in lst starting from 'start'
        for i in range(start, len(lst)):
            # Push the next state onto the stack: next index and updated path
            stack.append((path[:] + [lst[i]], i + 1))

    return result  # Exclude the empty set


def get_combinations_recurse(lst):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(lst)):
            backtrack(i + 1, path + [lst[i]])

    result = []
    backtrack(0, [])
    return result[1:]  # To exclude the empty set


print(get_combinations([1, 2, 3]))
