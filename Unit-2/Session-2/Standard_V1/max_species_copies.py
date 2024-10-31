"""As a conservationist, your research center has been raising multiple endangered species and is now ready to reintroduce them into their native habitats. You are given two 0-indexed strings raised_species and target_species. The string raised_species represents the list of species available to release into the wild at your center, where each character represents a different species. The string target_speciesrepresents a specific sequence of species you want to form and release together.

You can take some species from raised_species and rearrange them to form new sequences.

Return the maximum number of copies of target_species that can be formed by taking species from raised_species and rearranging them.
"""
def max_species_copies(raised_species, target_species):
    """
    P: Number of times the sequence of target species can be form from raised species
    E: 1. Target species length less than raised species length
    """
    
    # Create a set of target species
    target_species_set = set(target_species)
    
    # Create a map to track count of target species in raised species
    species_count = {}
    
    for specie in raised_species:
        if specie in target_species_set:
            species_count[specie] = species_count.get(specie, 0) + 1
    
    # Return min value of species in map
    return min(species_count.values())

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1