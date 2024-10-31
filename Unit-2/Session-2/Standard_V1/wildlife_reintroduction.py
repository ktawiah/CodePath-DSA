"""
As a conservationist, your research center has been raising multiple endangered species and is now ready to reintroduce them into their native habitats. You are given two 0-indexed strings raised_species and target_species. The string raised_species represents the list of species available to release into the wild at your center, where each character represents a different species. The string target_species represents a specific sequence of species you want to form and release together.

You can take some species from raised_species and rearrange them to form new sequences.

Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.
"""


def max_species_copies(raised_species, target_species):
    # Create specie count

    # Create a set of target species

    # Iterate through raised species

    # 


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2))  # Output: 2
