"""
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.
"""


def find_missing_clues(clues, lower, upper):
    """
    P: Create a list of all the ranges in of values missing in the clues
    """
    # Create set of clues
    clues_set = set(clues)

    # Create result list
    result = []

    # Iterate through clues
    index = lower
    while index < upper + 1:

        # Update result list
        if index not in clues_set:
            if not result or len(result[-1]) == 2:
                result.append([index])

            while len(result[-1]) == 1:
                if index in clues_set:
                    result[-1].append(index - 1)
                elif index == upper:
                    result[-1].append(upper)
                index += 1

        index += 1

    # Return result list
    return result


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
