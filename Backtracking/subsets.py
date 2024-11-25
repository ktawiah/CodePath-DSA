def subsets_iterative(nums):
    result = []
    stack = [(0, [])]  # Stack to store (start index, current path)

    while stack:
        start, path = stack.pop()  # Get the current state (index and subset)

        # Add the current subset to the result
        result.append(path)

        # Explore further subsets by adding one element at a time
        for i in range(start, len(nums)):
            # Create a new path by including nums[i]
            new_path = path + [nums[i]]
            stack.append((i + 1, new_path))  # Push the new state onto the stack

    return result


def backtrack(start, path, result, nums):
    # Add the current subset (path) to the result
    result.append(path[:])  # Make a copy of the current path

    # Explore further subsets by adding one element at a time
    for i in range(start, len(nums)):
        # Include nums[i] in the current subset
        path.append(nums[i])

        # Recursively generate all subsets starting from the next element
        backtrack(i + 1, path, result, nums)

        # Backtrack: remove the last element to explore other subsets
        path.pop()


def subsets(nums):
    result = []
    backtrack(0, [], result, nums)
    return result


# Example usage
nums = [1, 2, 3]
print(subsets(nums))
print(subsets_iterative(nums))
