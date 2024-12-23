def bs(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def bs_recurse(nums, target, left=0, right=None):
    if not right:
        right = len(nums) - 1

    if left > right:
        return left

    mid = (left + right) // 2

    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return bs_recurse(nums, target, left, right)


print(bs_recurse([1, 2, 3, 4, 4, 5], 4))
