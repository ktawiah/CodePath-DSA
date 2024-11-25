"""You are given an itinerary itinerary representing a list of trips between cities, where each city is represented by an integer.
We consider an itinerary valid if it is a permutation of an itinerary template base[n].

The template base[n] is defined as [1, 2, ..., n - 1, n, n] (in other words, it is an itinerary of length n + 1 that visits cities 1 to
n - 1 exactly once, plus visits city n twice). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return True if the given itinerary is valid, otherwise return False.

A permutation is an arrangement of a set of elements. For example [3, 2, 1] and [2, 3, 1] are both possible permutations of the set of numbers
1, 2, and 3.
"""


def is_valid_itinerary(itinerary):
    """
    P: Check if last city(max of itinerary) is visited twice and other cities visited once
    E: 1. Invalid itinerary list, len < max -> False
    2. No cities to visit -> False
    """
    # Check no city
    if len(itinerary) == 0:
        return False

    # Get the last city
    last_city = max(itinerary)

    # Check if len of itinerary is less than last city
    if len(itinerary)-1 != last_city:
        return False

    # Create a map of counts
    freq_map = {}
    for city in itinerary:
        freq_map[city] = freq_map.get(city, 0) + 1

    # Iterate through map
    for key, value in freq_map.items():

        # Return key with max count
        if (key == last_city and value != 2) or (key != last_city and value != 1):
            return False

    return True


itinerary1 = [2, 1, 3] # False
itinerary2 = [1, 3, 3, 2] # True
itinerary3 = [1, 1] # True

print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))
