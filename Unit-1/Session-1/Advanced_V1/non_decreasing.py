"""
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""


def non_decreasing(nums):
    deviation_count = 0

    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            deviation_count += 1

    return True if deviation_count < 2 else False


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))
