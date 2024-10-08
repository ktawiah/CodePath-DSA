def move_zeroes(nums):
    """
    P: Move all zeroes in list to the end

    [1,0,2,1,0,0] -> [1,2,1,0,0]
    [3,2,0,1] -> [3,2,1,0]

    S: 1. Create two pointers, fast and a slow pointer
    0 1 ->  Swap
    1, 0 -> Move fast
    1 1 -> Move both
    0 0 -> Move fast

    3. Continue while fast < length of nums
    """
    if len(nums) <= 1:
        return -1

    p1, p2 = 0, 1

    while p2 < len(nums):
        if nums[p1] == 0 and nums[p2] == 0:
            p2 += 1
        elif nums[p1] != 0 or nums[p2] == 0:
            p2 += 1
            p1 += 1
        elif nums[p1] != 0 and nums[p2] != 0:
            p1 += 1
            p2 += 1
        else:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1

    return nums


if __name__ == "__main__":
    print(move_zeroes([1, 0, 2, 0, 3, 0]))
    print(move_zeroes([1, 0, 2, 1, 0, 0]))
    print(move_zeroes([3, 2, 0, 1]))
