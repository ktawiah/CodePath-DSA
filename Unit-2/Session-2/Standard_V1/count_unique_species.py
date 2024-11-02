"""
You are given a string ecosystem_data that consists of digits and lowercase English letters. The digits represent the observed counts of various species in a protected ecosystem.

You will replace every non-digit character with a space. For example, "f123de34g8hi34" will become " 123 34 8 34". Notice that you are left with some species counts that are separated by at least one space: "123", "34", "8", and "34".

Return the number of unique species counts after performing the replacement operations on ecosystem_data.

Two species counts are considered different if their decimal representations without any leading zeros are different.
"""

from re import split


def count_unique_species(ecosystem_data):
    """
    P: Finding the number of unique, consecutive digits(species count) in ecosystem data
    E: 1. No ecosystem data
    """
    # Convert string data into a list
    data_list = list(ecosystem_data)

    # Iterate through the list data
    for index, specie in enumerate(data_list):
        # Replace current element with a space if not a digit
        if not specie.isdigit():
            data_list[index] = " "

    # Covert list back to string
    updated_string = "".join(data_list)

    # Split string into a list
    species_count = split(r"\s+", updated_string)

    # Remove duplicates
    unique_species = set()
    for specie in species_count:
        if specie:
            unique_species.add(int(specie))

    # Return count of elements in list
    return len(unique_species)


ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))
