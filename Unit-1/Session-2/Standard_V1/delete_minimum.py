def delete_minimum_elements(hunny_jar_sizes):
    """
    P: Return a list of sorted sizes by sequentially removing minimum element from list

    [3,2,1] -> [1,2,3]
    [5,3,1,2] -> [1,2,3,5]

    S: 1. Create placeholder for result list and placeholder for current minimum value
    2. Loop through list and keep track of min value's index
    3. Pop out minimum, append to result list
    4. Continue until list is empty
    5. Return result list
    """
    ordered_jar_sizes = []
    curr_min_value = float("inf")

    while len(hunny_jar_sizes) != 0:
        for index, num in enumerate(hunny_jar_sizes):
            if num < curr_min_value:
                curr_min_value = num
                min_index = index
        ordered_jar_sizes.append(curr_min_value)
        hunny_jar_sizes.pop(min_index)
        curr_min_value = float("inf")

    return ordered_jar_sizes


if __name__ == "__main__":
    print(delete_minimum_elements([5, 3, 2, 4, 1]))
    print(delete_minimum_elements([5, 2, 1, 8, 2]))
    print(delete_minimum_elements([3, 2, 1]))
