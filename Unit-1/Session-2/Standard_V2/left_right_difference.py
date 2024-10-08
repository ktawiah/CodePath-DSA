def left_right_difference(nums):
    """
    P: Return an answers list which contains a list of the difference between numbers from the left and those to the right of it

    [1,2,3] -> [-5,-2,0]

    S: 1. Create a placeholder for answers
    2. Loop through nums
    3. For each nums:
       - Determine sum to the left
       - Determine that to the right
       - Find diff
       - Append to answers
    4. Return answers
    """
    answers = []

    for index, num in enumerate(nums):
        sum_left = 0

        for i in range(index):
            sum_left += nums[i]

        sum_right = 0

        for i in range(index + 1, len(nums)):
            sum_right += nums[i]
        answers.append(sum_left - sum_right)

    return answers


nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))
