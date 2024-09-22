def sum_honey(hunny_jars):
    """
    P: Determine the sum of all elements in an input list

    [1,2,3] -> 6
    [] -> 0
    [1] -> 1

    S: 1. Create a placeholder for result_sum and initialize to 0
    2. Loop through the list and add each element to the sum
    """
    result_sum = 0
    for jar in hunny_jars:
        result_sum += jar
    return result_sum


if __name__ == "__main__":
    print(sum_honey([2, 3, 4, 5]))
    print(sum_honey([]))
