def running_sum(superhero_stats):
    """
    P: Return a list of cumulative sums in superhero stats list

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
