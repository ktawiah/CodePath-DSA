"""
In your time travel adventures, you are given an array of digit strings portals and a digit
string destination. Return the number of pairs of indices (i, j) (where i != j) such that
the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order
matters.

"""


def num_of_time_portals(portals, destination):
    from collections import Counter

    # Count occurrences of each portal string
    portal_count = Counter(portals)
    print(portal_count)
    pair_count = 0

    # Iterate through each portal
    for portal in portals:
        required = destination[len(portal):]  # The part of destination after the current portal
        if required in portal_count:
            pair_count += portal_count[required]

            # If the required portal is the same as the current one, we need to subtract one
            if required == portal:
                pair_count -= 1

    return pair_count

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
