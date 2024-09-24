def good_pairs(pile1, pile2, k):
    """
    P: Determine two sticks from pile1 and pile2 which satisfy the criteria x1 % (x2 + k) == 0

    [1,2,3,5,8], [1,2,3], 1 -> (0, 1), (2, 1)

    S: 1. Loop through first list
    2. Loop through the second, with index
    3. Compare elements and update count
    4. Return number of pairs.
    """
    pair_count = 0
    for num1 in pile1:
        for num2 in pile2:
            if num1 % (num2 * k) == 0:
                pair_count += 1

    return pair_count


if __name__ == "__main__":
    print(good_pairs([1, 3, 4], [1, 3, 4], 1))
    print(good_pairs([1, 2, 4, 12], [2, 4], 3))
