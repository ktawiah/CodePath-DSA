"""
Captain Dread is keeping track of the crew's activities using a log. The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] indicates that the pirate with pirateID performed an action at the minute time.

Multiple pirates can perform actions simultaneously, and a single pirate can perform multiple actions in the same minute.

The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate performed an action. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.

Return the array answer as described above.
"""

def counting_pirates_action_minutes(logs, k):
    # Create map to store pirate unique minutes
    pirate_minutes = {}

    for pirate, minutes in logs:
        if pirate not in pirate_minutes: 
            pirate_minutes[pirate] = pirate_minutes.get(pirate, set())
        pirate_minutes[pirate].add(minutes)


    # # Create list of size k
    result_list = [0] * k

    # Iterate through map values and update result list
    for value in pirate_minutes.values():
        result_list[len(value)-1] += 1

    return result_list

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
