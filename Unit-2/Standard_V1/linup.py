def lineup(artists, set_times):
    """
    P: Represent two lists as dict

    [1,2,3], ["me", "you", "us"] -> {1: "me", 2: "you", 3: "us"}

    S: 1. Create pointers for both lists
    2. While either less than length resp. list
     - Create key, value pairs in the dict
    3. Return dict
    """
    dict_map = {}

    p1, p2 = 0, 0

    while p1 < len(artists) and p2 < len(set_times):
        dict_map[artists[p1]] = set_times[p2]
        p1 += 1
        p2 += 1

    return dict_map


if __name__ == "__main__":
    print(
        lineup(
            ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"],
            ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"],
        )
    )
