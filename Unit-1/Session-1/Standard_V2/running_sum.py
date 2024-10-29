"""
Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). You must modify the list in place; you may not create any new lists as part of your solution.
"""


def running_sum(superhero_stats):
    """
    P: Replace elements in list by sum of previous element and itself

    [1,2,3] -> [1,3,6]
    [0,2,3] -> [0,2,5]

    S: 1. Create placeholder for cumulative sum
    2. Loop through stats
    3. Add previous stat to current stat and assign to cumulative sum
    4. Update current value with sum
    5. Return updated stats
    """

    if len(superhero_stats) <= 1:
        return superhero_stats

    for idx in range(1, len(superhero_stats)):
        c_sum = superhero_stats[idx - 1] + superhero_stats[idx]
        superhero_stats[idx] = c_sum

    return superhero_stats


if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))
    print(running_sum([1, 1, 1, 1, 1]))
    print(running_sum([3, 1, 2, 10, 1]))
    print(running_sum([1]))
