def best_set(votes):
    """
    1. Keep track of key with max value using dictionary
    2. Return the value
    """
    # result_dict = {}
    max_value = float("-inf")
    max_key = 0
    for key in votes.keys():
        if key > max_value:
            max_key = key

    return votes[max_key]


votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA",
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
}

print(best_set(votes1))
print(best_set(votes2))
