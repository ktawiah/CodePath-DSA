"""
Write a function smaller_than_current that accepts a list of integers nums and, for each element in the list nums[i], determines the number of other elements in the array that are smaller than it. More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer as a list.
"""


def smaller_than_current(nums):
    # Create a result list
    results = []

    # Iterate through elements in nums
    for index, num in enumerate(nums):

        # Create a counter for nums less than current value
        counter = 0

        # Create copy of nums and remove current value from it
        nums_copy = nums[:]
        nums_copy.pop(index)

        for val in nums_copy:
            if val < num:
                counter += 1

        # Update result list
        results.append(counter)

    # Return result list
    print(results)


nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)
