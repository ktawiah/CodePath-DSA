"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.
"""


def count_endangered_species(endangered_species, observed_species):
    # Create a set of endangered species
    endangered_set = set(endangered_species)

    # Create a frequency map for specie count
    freq_map = {}

    # Iterate through observed species
    for specie in observed_species:

        # Update map
        if specie in endangered_set:
            freq_map[specie] = freq_map.get(specie, 0) + 1

    # Return sum counts
    return sum(freq_map.values())


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))
