def good_pairs(pile1, pile2, k):
    """
    P: Determine the number of good pairs in both stick piles which follow the following constraint p1 % (p2 + k) == 0

    [5,8, 9], [1,2,3,4], 1 -> 4

    S: 1. Create placeholder for good pair count
    2. Loop through pile2, then pile1
    3. If constraint met, increment count by 1 else do nothing
    4. Return count
    """
    count = 0

    for stick2 in pile2:
        for stick1 in pile1:
            # print(stick2, stick1)
            if stick1 % (stick2 + k) == 0:
                count += 1

    print(count)


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)
