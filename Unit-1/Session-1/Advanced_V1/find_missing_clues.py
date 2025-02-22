"""
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.
"""


def find_missing_clues(clues, lower, upper):
    """
    -> Understanding
    [0, 1, 3, 50, 75], 0, 90 -> [[2, 2], [4, 49], [51, 74], [76, 90]]
    P: Determine the ranges of clues missing from trail

    0. Create placeholder to store result
    1. Keep track of expected next value
    2. If expected next value is not equal to current value
        2.1. Create a placeholder for curr missing range
        2.2. Add curr expected to result
        2.3. Add next val-1 to result
    3. Check if end of trail is missing
        3.1. Add trail range to result list
    4. Return result list
    """

    n = len(clues)
    # 0. Create placeholder to store result
    missing_clues = []

    if not clues:
        return missing_clues

    # Handle start of clues missing
    if lower < clues[0]:
        missing_clues.append([lower, clues[0] - 1])

    # 1. Keep track of expected next value
    expected = clues[0] + 1

    for i in range(1, n):
        # 2. If expected next value is not equal to current value
        if expected != clues[i]:
            #     2.1. Create a placeholder for curr missing range
            sub_range = []

            #     2.2. Add curr expected to result
            sub_range.append(expected)

            #     2.3. Add next val-1 to result
            sub_range.append(clues[i] - 1)

            expected = clues[i] + 1
            missing_clues.append(sub_range)
        else:
            expected += 1

    # 3. Check if end of trail is missing
    if clues[-1] < upper:

        #   3.1. Add trail range to result list
        missing_clues.append([clues[-1] + 1, upper])

    # 4. Return result list
    return missing_clues

    # """
    # P: Create a list of all the ranges in of values missing in the clues
    # """
    # # Create set of clues
    # clues_set = set(clues)

    # # Create result list
    # result = []

    # # Iterate through clues
    # index = lower
    # while index < upper + 1:

    #     # Update result list
    #     if index not in clues_set:
    #         if not result or len(result[-1]) == 2:
    #             result.append([index])

    #         while len(result[-1]) == 1:
    #             if index in clues_set:
    #                 result[-1].append(index - 1)
    #             elif index == upper:
    #                 result[-1].append(upper)
    #             index += 1

    #     index += 1

    # # Return result list
    # return result


clues = [1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))  # [[2,2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
