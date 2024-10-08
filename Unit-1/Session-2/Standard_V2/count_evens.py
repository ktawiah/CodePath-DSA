def count_evens(lst):
    """
    P: Return count of all the string of even length in lst

    ["me", 'aba', "rece"] -> 2
    [] -> 0

    S: 1. Create placeholder for correct string count
    2. Loop through list
    3. Check length of each string
    4. Increment counter by 1 if len is even else do nothing
    5. Return
    """
    count = 0

    for string in lst:
        if len(string) % 2 == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(count_evens(["na", "nana", "nanana", "batman", "!"]))
    print(count_evens(["the", "joker", "robin"]))
    print(
        count_evens(
            [
                "you",
                "either",
                "die",
                "a",
                "hero",
                "or",
                "you",
                "live",
                "long",
                "enough",
                "to",
                "see",
                "yourself",
                "become",
                "the",
                "villain",
            ]
        )
    )
    print(count_evens(["me", "aba", "rece"]))
