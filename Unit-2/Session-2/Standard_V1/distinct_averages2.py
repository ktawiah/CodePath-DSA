"""
You are given a 0-indexed integer array species_populations, where each element represents the population of a particular species in a wildlife reserve.

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
    """
    P: Return a list of averages of the largest and smallest population from species_populations
    [1,2,3] -> [2, 1]
    E: 1. What if at any point the length of list is <= 1
    """
    # Create a list to store averages
    averages = []
    
    # Follow steps and handle edge cases
    while species_populations:
        max_population = max(species_populations)
        species_populations.remove(max_population)
        min_population = min(species_populations) if species_populations else -1
        if min_population != -1:
            species_populations.remove(min_population)
        else:
            min_population = 0
        curr_average = (max_population + min_population) / 2
        averages.append(curr_average)
    
    # Return list of averages
    return averages

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 
print(distinct_averages([1, 2, 3]))