def counting_sort(nums):
    sorted_nums = [0] * max(nums)

    for num in nums:
        sorted_nums[num - 1] += 1

    nums.clear()

    for index, num in enumerate(sorted_nums):
        while num > 0:
            nums.append(index + 1)
            num -= 1

    return nums


print(counting_sort([3, 2, 3, 5, 1, 90]))
