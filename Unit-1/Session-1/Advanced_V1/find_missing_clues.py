def find_missing_clues(clues, lower, upper):
    """
    P: Create a list of all the ranges in of values missing in the clues

    S: 1. Convert clues to set
    2. Create result list, current range list
    2. Loop from lower to upper
    2. while num is not in clues set:
      add num to current range list
      While range set is not empty:
        - add current value - 1
        - append to result set
        - empty list
    4. Return result list
    """
    pass
    # clues_set = set(clues)

    # results = []
    # curr_range = []

    # if len(clues) <= 1:
    #     return clues[0]

    # if lower not in clues_set:
    #     curr_range.append(clues[0])

    # print(curr_range)

    # all_clues = list(range(lower, upper + 1))

    # # print(all_clues[1:])

    # # for clue in all_clues:
    # #     if clue not in clues_set and len(curr_range) == 0:
    # #         curr_range.append(clue)

    # #     if (
    # #         clue not in clues_set
    # #         and len(curr_range) == 1
    # #         and clues[clues.index(clue + 1)] in clues_set
    # #     ):
    # #         curr_range.append(clue)
    # #         results.append(curr_range)
    # #         curr_range.clear()

    # for index in range(lower, upper+1):
    #     if index not in clues_set and len(curr_range) == 0:
    #         curr_range.append(index)

    #     if

    # return results


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
