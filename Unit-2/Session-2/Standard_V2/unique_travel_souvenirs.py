"""As a seasoned traveler, you've collected a variety of souvenirs from different destinations. You have an array of string souvenirs, where each string represents a type of souvenir. You want to know if the number of occurrences of each type of souvenir in your collection is unique.

Write a function that takes in an array souvenirs and returns True if the number of occurrences of each value in the array is unique, or False otherwise."""


def unique_souvenir_counts(souvenirs):
    # Handle no souvenirs case
    if len(souvenirs) == 0:
        return False

    # Create a map of souvenir counts
    souvenir_counts = {}
    for souvenir in souvenirs:
        souvenir_counts[souvenir] = souvenir_counts.get(souvenir, 0) + 1

    # Get set of counts
    count_set = set(souvenir_counts.values())

    # Compare len of set to that of len of counts
    return len(count_set) == len(souvenir_counts.values())


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]  # True
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]  # True
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]  # False

print(unique_souvenir_counts(souvenirs1))
print(unique_souvenir_counts(souvenirs2))
print(unique_souvenir_counts(souvenirs3))
