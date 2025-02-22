"""Problem 5: Group Animals by Habitat
You are managing a wildlife sanctuary where animals of the same species need to be grouped together by their habitats. Given a string habitats representing the sequence of animals, where each character corresponds to a particular species, you need to partition the string into as many contiguous groups as possible, ensuring that each species appears in at most one group.

The order of species in the resultant sequence must remain the same as in the input string habitats.

Return a list of integers representing the size of these habitat groups."""


def group_animals_by_habitat(habitats):
    # Step 1: Record the last occurrence of each species
    last_occurrence = {}
    for i, species in enumerate(habitats):
        last_occurrence[species] = i

    # Step 2: Initialize variables for the result and to track the partitioning process
    result = []
    start = 0
    end = 0

    # Step 3: Traverse the string and form groups
    for i, species in enumerate(habitats):
        # Update the farthest point we need to reach in the current group
        end = max(end, last_occurrence[species])

        # If we've reached the farthest point for this group, it forms a valid group
        if i == end:
            result.append(i - start + 1)  # Size of the current group
            start = i + 1  # Start the next group

    return result


# Example cases
print(
    group_animals_by_habitat("ababcbacadefegdehijhklij")
)  # Expected output: [9, 7, 8]
print(group_animals_by_habitat("eccbbbbdec"))  # Expected output: [10]

print(group_animals_by_habitat("ababcbacadefegdehijhklij"))
print(group_animals_by_habitat("eccbbbbdec"))

[9, 7, 8]
[10]
