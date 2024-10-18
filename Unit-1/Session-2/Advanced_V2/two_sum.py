"""
Use the two pointer approach to implement a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.
"""

# def two_sum(nums, target):
#     diff_map = {}

#     for index, num in enumerate(nums):
#         diff = target - num

#         if num in diff_map:
#             return [diff_map.get(num), index]
#         else:
#             diff_map[diff] = index

#     return []


def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    end = 0

    while end < len(arr):
        windowSum += arr[end]

        if (end - start + 1) == k:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1

        end += 1

    return maxSum


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))
