"""
Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.

Return the minimum number of steps to make map2 an anagram of map1.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""

def min_steps_to_match_maps(map1, map2):
    # Create freq_maps for both maps
    freq_map1 = {}
    freq_map2 = {}

    # Create a placeholder for steps
    steps = 0

    # Iterate through either maps and update freq_maps
    for char in map1:
        freq_map1[char] = freq_map1.get(char, 0) + 1

    for char in map2:
        freq_map2[char] = freq_map2.get(char, 0) + 1

    # Update steps
    for char, count in freq_map1.items():
        required = freq_map1.get(char)
        present = freq_map2.get(char, 0)

        if (required > present):
            steps += required - present

    # Return steps
    return steps

""" Wrong and inefficient brute force solution
from copy import deepcopy
def min_steps_to_match_maps(map1, map2):
    # Convert map1 in to list
    map1_list = list(map1)

    # Create a count
    count = 0

    # Iterate through map2
    for char in map2:
        
        # Update count and list
        curr_list = deepcopy(map1_list)
        for index, curr in enumerate(map1_list):
            if curr == char:
                map1_list.pop(index)

        if len(curr_list) == len(map1_list):
            count += 1

    # Return count
    return count

"""

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
