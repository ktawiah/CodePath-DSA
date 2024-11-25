from typing import List


def get_combinations(lst):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(lst)):
            backtrack(i + 1, path + [lst[i]])

    result = []
    backtrack(0, [])
    return result[1:]  # To exclude the empty set


def get_permutations(lst):
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])

    result = []
    backtrack([], lst)
    return result


def get_max_memory(memory: List[int]) -> int:
    """
    P: Determine the max memory gained from prefix sum of combination from memory
    """

    # Create a list to store all combinations
    comb_list = get_permutations(memory)

    # Iterate through each element
    #  convert to prefix sum array
    for comb in comb_list:
        for i in range(1, len(comb)):
            comb[i] += comb[i - 1]

    # Update val with sum of prefix sum
    for index, num in enumerate(comb_list):
        comb_list[index] = sum(num)

    # Return max sum
    return max(comb_list)


print(get_max_memory([3, 4, 5]))
