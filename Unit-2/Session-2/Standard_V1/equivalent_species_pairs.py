"""In an effort to understand species diversity in different habitats, researchers are analyzing species pairs 
observed in various regions. Each pair is represented by a list [a, b] where a and b represent two species observed together.

A species pair [a, b] is considered equivalent to another pair [c, d] 

if and only if either (a == c and b == d) or (a == d and b == c).

 This means that the order of species in a pair does not matter.

Your task is to determine the number of equivalent species pairs in the list of observed species pairs.
"""


def num_equiv_species_pairs(species_pairs):
    """
    P: Problem Definition
      - For any species pair [a,b], [c,d] in species pairs, determine the number of equivalent species
      - Meaning a==c and b==d, or a==d and b==c
      - For both pairs to be unique, each element in first pair must be found in the other

    I: Input/Output
      - Input -> List[List[ints]] an Output -> int

      Example: [[1, 2], [2, 1], [3, 4], [5, 6]] -> 1

    C: Edge Cases
      - No pairs, Empty -> 0
      - One pair -> 0

    A: Approach/Algorithm
      - Handle edge cases
      - Create a counter to keep track of equivalent pairs
      - Iterate through the species pairs
      - Compare current pair to next pairs -> n -> n+1..len(s_p), set(first) == set(second)
      - Updating a counter
      - Return the counter

    S: Solve/Implementation
      - Done

    S: Study/Analyse
      - Time complexity -> O(n^2)
      - Space complexity -> O(1)

    O: Optimize
      - Optimal since each element should be compared with all other elements to determine whether the pair is equivalent
    """
    if len(species_pairs) < 2:
        return 0

    # Create a counter to keep track of equivalent pairs
    count = 0

    # Iterate through the species pairs
    for index, f_pair in enumerate(species_pairs):  # O(n)
        for s_pair in species_pairs[index + 1 :]:  # O(n-1)
            # Compare current pair to next pairs -> n -> n+1..len(s_p), set(first) == set(second)
            if set(f_pair) == set(s_pair):  # O(1)
                count += 1

    return count


species_pairs1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
species_pairs2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))
