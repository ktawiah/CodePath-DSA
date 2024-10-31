"""
Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

Return a list of groups such that each pirate i is in a group of size group_sizes[i].

Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""

def organize_pirate_crew(group_sizes):
    # Create result list
    result = []
    
    # Create a map with a list of ids of members of each group size
    size_members = {}

    # Iterate through map
    for index, size in enumerate(group_sizes):
        size_members[size] = size_members.get(size, []) + [index]

    # Break list based on sized and append to result list
    for key, value in size_members.items():
        start = 0
        group_list = list(value)
        end = start + key
        while end < len(group_list):
            result.append(group_list[start:end])
            start += key
            end = start + key

        if end+1 > len(group_list):
            result.append(group_list[start:])

    # Return result list
    return result

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
