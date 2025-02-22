"""Problem 2: Pair Up Animals for Shelter
In an animal shelter, animals are paired up to share a room. Each pair has a discomfort level, which is the sum of their individual discomfort levels. The shelter's goal is to minimize the maximum discomfort level among all pairs to ensure that the rooms are as comfortable as possible.

Given a list discomfort_levels representing the discomfort levels of n animals, where n is even, pair up the animals into n / 2 pairs such that:

Each animal is in exactly one pair, and
The maximum discomfort level among the pairs is minimized. Return the minimized maximum discomfort level after optimally pairing up the animals.
Return the minimized maximum comfort level after optimally pairing up the animals."""


def pair_up_animals(discomfort_levels):
    discomfort_levels.sort()

    start, end = 0, len(discomfort_levels) - 1

    max_discomfort_level = float("-inf")

    while start < end:
        max_discomfort_level = max(
            max_discomfort_level, discomfort_levels[start] + discomfort_levels[end]
        )
        start += 1
        end -= 1

    return max_discomfort_level


print(pair_up_animals([3, 5, 2, 3]))
print(pair_up_animals([3, 5, 4, 2, 4, 6]))

7
8
