"""
Captain Feathersword and their crew has discovered a list of gold amounts at various
hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

Given an array of integers gold_amounts representing the amount of gold at each location
and an integer target, return the indices of the two locations whose gold amounts add up
to the target.

Assume that each input has exactly one solution, and you may not use the same location
twice. You can return the answer in any order.
"""

def find_treasure_indices(gold_amounts, target):
    """
    P: Return indices of gold amounts that sum up to target
    """

    # Create amount_index map
    amount_index = {}

    # Iterate through amounts input
    for index, amount in enumerate(gold_amounts):
        diff = target - amount

        # Update map
        if amount not in amount_index:
            amount_index[diff]= index
        else:
            return [amount_index.get(amount), index]

    # Return indices
    return [-1, -1]

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3)) 
