def count_endangered_species(endangered_species, observed_species):
    """
        endangered_species1 = "aA"
    observed_species1 = "aAAbbbb"

        P: Determine the number of endangered of endangered species observed
    """
    counter = 0

    species_dict = {}

    for specie in observed_species:
        species_dict[specie] = species_dict.get(specie, 0) + 1

        # if specie not in species_dict:
        #     species_dict[specie] = 1
        # else:
        #     species_dict[specie] = species_dict.get(specie) + 1

    for specie in endangered_species:
        if specie in species_dict.keys():
            counter += species_dict.get(specie)

    return counter


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))
