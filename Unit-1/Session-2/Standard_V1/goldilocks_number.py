def goldilocks_approved(nums):
    """
    P: Determine the number in nums that's between minimum and maximum value

    [1,2] -> -1
    [1,2,3] -> 2
    [1,2,3,4] -> 2

    S: 1. Find min number
    2. Loop through list
    3. Create placeholder for result
    4. Determine number that's just above the minimum value
    """
    min_value = min(nums)

    result = float("inf")

    if len(nums) <= 2:
        return -1

    for num in nums:
        if num < result and num != min_value:
            result = num

    return result


if __name__ == "__main__":
    print(goldilocks_approved([3, 2, 1, 4]))
    print(goldilocks_approved([1, 2]))
    print(goldilocks_approved([2, 1, 3]))
