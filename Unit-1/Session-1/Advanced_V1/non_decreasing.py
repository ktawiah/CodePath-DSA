def non_decreasing(nums):
    deviation_count = 0

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            deviation_count += 1

    return True if deviation_count <= 1 else False


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))
