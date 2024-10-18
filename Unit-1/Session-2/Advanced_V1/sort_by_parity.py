"""
Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


def sort_by_parity(nums):

    if len(nums) < 2:
        return nums

    start = 0
    end = 1

    while end < len(nums):
        if (nums[start] % 2 == 0 and nums[end] % 2 == 0) or (
            nums[start] % 2 == 0 and nums[end] % 2 == 1
        ):
            start += 1
            end += 1
        elif nums[start] % 2 == 1 and nums[end] % 2 == 0:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end += 1
        else:
            end += 1

    return nums


nums = [3, 1, 2, 4]
# nums = [3, 1, 2, 4, 9, 6, 8, 10, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))
