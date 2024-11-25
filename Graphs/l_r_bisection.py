def binary_search_left(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(binary_search_left([1, 2, 2, 2, 3, 4, 5, 7], 2))
