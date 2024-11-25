def get_subset(nums):
    result = []
    stack = [([], 0)]

    while stack:
        subset, index = stack.pop()
        result.append(subset)

        for idx in range(index + 1, len(nums)):
            stack.append((subset[:] + [idx], idx))

    print(result)


get_subset([1, 2, 3, 4])
