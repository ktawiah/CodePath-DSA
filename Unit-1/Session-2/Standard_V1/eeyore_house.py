"""
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.
"""


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
