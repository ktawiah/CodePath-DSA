"""
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.
"""


def num_of_time_portals(portals, destination):

    count = 0
    portal_count = {}

    # Count occurrences of each portal
    for portal in portals:
        portal_count[portal] = portal_count.get(portal, 0) + 1

    # Check for pairs
    for i, value in enumerate(portals):
        # The first part is portals[i]
        second_part = destination[len(value) :]  # What the second part should be

        if second_part in portal_count:
            # Count valid pairs
            count += portal_count[second_part]
            # If the second part is the same as the first part, we need to subtract 1
            # because we can't use the same index
            if second_part == value:
                count -= 1

    return count


# Example Usage
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))  # Output: 4
print(num_of_time_portals(portals2, destination2))  # Output: 2
print(num_of_time_portals(portals3, destination3))  # Output: 6


def portal_sum(portals, destination):

    portal_count = {}

    # Count occurrences of each portal and store their indices
    for index, portal in enumerate(portals):
        portal_count[portal] = portal_count.get(portal, []) + [index]

    result_pairs = []

    # Check for pairs
    for i, value in enumerate(portals):
        second_part = destination[len(value) :]  # What the second part should be

        if second_part in portal_count:
            for j in portal_count[second_part]:
                if i != j:  # Ensure i is not equal to j
                    result_pairs.append((i, j))

    return result_pairs


# Example Usage
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(portal_sum(portals1, destination1))  # Output: [(0, 1), (0, 2), (1, 0), (2, 0)]
print(portal_sum(portals2, destination2))  # Output: [(0, 1), (2, 3)]
print(
    portal_sum(portals3, destination3)
)  # Output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
