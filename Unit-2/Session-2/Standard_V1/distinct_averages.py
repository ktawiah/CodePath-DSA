"""
You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.
"""


def distinct_averages(species_populations):
    # Create list to store resp. averages
    averages = set()

    # Iterate through species
    while len(species_populations) != 0:

        # Determine the average and update averages list
        average = (min(species_populations) + max(species_populations)) // 2
        species_populations.remove(min(species_populations))
        species_populations.remove(max(species_populations))

        averages.add(average)

    # Return averages list
    return len(averages)


species_populations1 = [4, 1, 4, 0, 3, 5]
species_populations2 = [1, 100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2))
