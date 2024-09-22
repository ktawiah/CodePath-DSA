def count_less_than(race_times, threshold):
    """
    P: Determine the number of sticks that fall under the threshold

    [2,3,4,2], 3 -> 2
    [] -> 0
    [1,2,3,9], 9 -> 3

    s: 1. Create a placeholder to store count of sticks under limit
    2. Loop through the race_times
    3. Increment count if race is less that threshold else do nothing
    4. Return count
    """

    count = 0
    for time in race_times:
        if time < threshold:
            count += 1

    return count


if __name__ == "__main__":
    print(count_less_than([1, 2, 3, 4, 5, 6], 4))
    print(count_less_than([], 4))
