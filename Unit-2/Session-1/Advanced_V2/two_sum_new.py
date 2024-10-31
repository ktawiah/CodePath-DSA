def two_sum(nums, target):
    # Create a freq map
    freq_map = {}
    result_list = []
    count = 0

    # Iterate through nums
    for index, num in enumerate(nums):
        diff = target - num
        if freq_map.get(diff) == index:
            result_list.pop()
            count -= 1

        if diff in freq_map:
            result_list.append((index, diff))
            result_list.append((diff, index))
            count += 2
        else:
            freq_map[num] = index

    print(freq_map, count, result_list)


two_sum([1, 1, 1], 2)
