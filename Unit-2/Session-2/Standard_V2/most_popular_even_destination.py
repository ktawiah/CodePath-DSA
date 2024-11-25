"""Given a list of integers destinations, where each integer represents the popularity score of a destination, return the most popular even destination.

If there is a tie, return the smallest one. If there is no such destination, return -1.
"""
def most_popular_even_destination(destinations):
    """
    P: Determine even destination with the highest count
    E: 1. When tie in counts of even -> Return smallest
        2. No destination -> -1
    """
    # Create a freq map for even destinations
    even_counts = {}

    # Iterate through destinations
    for destination in destinations:

        # Update the map with even distributions
        if destination % 2 == 0:
            even_counts[destination] = even_counts.get(destination, 0) + 1

    # Return -1 if map is empty
    if not even_counts:
        return -1

    # Get max count from map
    max_count = max(even_counts.values())

    # Return key
    for destination, value in even_counts.items():
        if value == max_count:
            return destination

    return -1


destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))


# 2
# 4
# -1