"""
Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


def sort_by_parity(nums):
    new_list = []

    first_even = 0

    for num in nums:
        if num % 2 == 0:
            new_list.insert(first_even, num)
            first_even += 1
        else:
            new_list.append(num)

    return new_list


nums = [3, 1, 2, 4]
# nums = [3, 1, 2, 4, 9, 6, 8, 10, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))
