"""You are managing an animal adoption center, and you have two lists of animals: available and preferred, both consisting of lowercase English letters representing different types of animals.

Return the minimum number of characters that need to be appended to the end of the available list so that preferred becomes a subsequence of available.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters."""


def append_animals(available, preferred):

    if len(preferred) > len(available):
        return -1

    available_set = set(available)

    start = 0

    while start < len(preferred):

        if preferred[start] not in available_set:
            break

        start += 1

    return len(preferred) - start


print(append_animals("catsdogs", "cows"))
print(append_animals("rabbit", "r"))
print(append_animals("fish", "bird"))

2
0
4
