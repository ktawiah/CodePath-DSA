def remove_duplicates(nums):
    if len(nums) < 2:
        return nums

    start = 0
    end = 1

    while end < len(nums):
        if nums[start] == nums[end]:
            nums.pop(start)
        else:
            start += 1
            end += 1

    return nums


print(remove_duplicates([1, 2, 2, 3, 4, 5]))
