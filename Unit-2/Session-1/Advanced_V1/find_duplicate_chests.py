"""
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.
"""


def find_duplicate_chests(chests):
    # Create frequency map
    freq_map = {}

    # Create result list
    results = []

    # Iterate through chests
    for num in chests:
        # Update map
        freq_map[num] = freq_map.get(num, 0) + 1

    # Iterate through map
    for key, val in freq_map.items():
        # Update result list with val with freq > 1
        if val > 1:
            results.append(key)

    # Return result list
    return results


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
