def squared(numbers):
    """
    P: Return numbers with all its elements squared

    [1,2,3] -> [1, 4, 6]
    [1] -> 1
    [0] -> 0
    [] -> []

    S: 1. Create a placeholder for squared_value
    2. Loop through numbers
    3. Square number and assign to square value placeholder
    4. Replace current number with placeholder value and reset square_value
    5. Return numbers
    """
    square_value = 1

    for index, num in enumerate(numbers):
        square_value = num**2
        numbers[index] = square_value
        square_value = 1

    return numbers


if __name__ == "__main__":
    print(squared([1, 2, 3]))
    print(squared([]))
    print(squared([0]))
