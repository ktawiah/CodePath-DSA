def make_divisible_by_3(nums):
    """
    P: Return minimum number of operations performed on each element to make it divisible by 3

    [1,2,3] -> 2

    [5, 3, 1] -> 2

    S: 1. Create placeholder for total min and current min
    2. Loop through nums
    3. Check if curr num is divisible by; go back to first loop if it is
    4. while num is not divisible by 3:
      - Perform both operations
      - Increment curr min
      - Check divisibility
      - Add min to total
    """
    total_min = 0

    for num in nums:
        if num % 3 == 0:
            continue

        sub_num = num
        add_num = num
        curr_min_add = 0
        curr_min_sub = 0
        while num % 3 != 0:
            if (sub_num - 1) % 3 != 0:
                curr_min_sub += 1
            else:
                total_min += curr_min_sub
                curr_min_sub = 0
                break

            if (add_num + 1) % 3 != 0:
                curr_min_add += 1
            else:
                total_min += curr_min_add
                curr_min_add = 0
                break

    return total_min


if __name__ == "__main__":
    print(make_divisible_by_3([1, 2, 3, 4]))
    print(make_divisible_by_3([3, 6, 9]))
