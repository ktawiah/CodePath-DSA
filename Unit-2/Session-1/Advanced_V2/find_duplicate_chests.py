"""
Captain Blackbeard has an integer array chests of length n where all the integers
in chests are in the range [1, n] and each integer appears once or twice.
Return an array of all the integers that appear twice, representing the treasure
chests that have duplicates.
"""

def find_duplicate_chests(chests):
    """
    P: Return a list of integers with count == 2
    """

    # Create a freq_map
    freq_map = {}

    for num in chests:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Create result list
    result = []

    # Iterate through freq_map
    for key, value in freq_map.items():
        
        # Update result list
        if value == 2:
            result.append(key)

    # Return result list
    return result

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
