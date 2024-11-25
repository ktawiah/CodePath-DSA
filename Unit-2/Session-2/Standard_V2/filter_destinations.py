"""You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.
"""


def remove_low_rated_destinations(destinations, rating_threshold):
    """
    P: - Return a map of all destination whose ratings are >= threshold
    I: {a: 5, b: 7, c: 5, d: 4}, 5 ->  {a.., b.., c..}
      {} ->
    C: - No destination -> {}

    A: - Create a copy of destinations map
      - Iterate through the copy -> 0(n)
      - Remove all key, value pairs with with rating less than threshold -> 0(1)
      - Return destination map -> 0(1)

      {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}, 4.0 -> {"Paris": 4.8, "Addis Ababa": 4.9}
    S: Done
    S: Time Complexity: 0(n), Space Complexity: 0(1)
    O: Optimal solution because iteration must be done for comparison to be made
    """

    init_keys = destinations.copy().keys()

    for destination in init_keys:
        if destinations.get(destination) < rating_threshold:
            destinations.pop(destination)

    return destinations


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))
