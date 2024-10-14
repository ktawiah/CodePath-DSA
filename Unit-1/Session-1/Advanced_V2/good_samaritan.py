"""
Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.
"""


def minimum_boxes(meals, capacity):
    # Create placeholder for min_boxes
    min_boxes = 0

    # Determine the total number of meals
    total_meals = sum(meals)

    # Sort capacity
    sorted_capacity = sorted(capacity)

    # Check min boxes to carry all meals
    new_sum = 0

    while new_sum < total_meals:
        min_boxes += 1
        new_sum += sorted_capacity.pop()

    print(min_boxes)


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
