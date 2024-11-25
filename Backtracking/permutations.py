def get_permutations(lst):
    result = []
    stack = [([], lst)]  # Stack holds tuples of (current path, remaining elements)

    while stack:
        path, remaining = stack.pop()

        if not remaining:
            result.append(path)
        else:
            for i in range(len(remaining)):
                # Append a new state to the stack for the next step
                stack.append(
                    (path + [remaining[i]], remaining[:i] + remaining[i + 1 :])
                )

    return result


def get_permutations_recurse(lst):
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])

    result = []
    backtrack([], lst)
    return result


print(get_permutations([1, 2, 3]))
