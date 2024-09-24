def get_odds(nums):
    """
    P: Return a list of all odd numbers in nums

    [1,2,3] -> [1,3]
    [1] -> [1]
    [2] -> []

    S: 1. Create a placeholder for odd numbers
    2. Loop through list
    3. Add to odd_nums if element is odd else do nothing
    4. Return odd_nums
    """
    odd_nums = []

    for num in nums:
        if num % 2 == 1:
            odd_nums.append(num)

    return odd_nums


if __name__ == "__main__":
    print(get_odds([1, 2, 3, 4]))
    print(get_odds([2, 4, 6, 8]))
