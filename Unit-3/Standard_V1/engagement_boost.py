"""You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements 

***sorted in non-decreasing order***, 

return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique."""


def engagement_boost(engagements):
    result = [0] * len(engagements)
    curr_pos = len(result) - 1
    start, end = 0, len(engagements) - 1

    while start <= end:
        if -engagements[start] > engagements[end]:
            result[curr_pos] = (-engagements[start]) ** 2
            start += 1
        else:
            result[curr_pos] = engagements[end] ** 2
            end -= 1

        curr_pos -= 1

    return result

    # squared_engagements = []

    # for i in range(len(engagements)):
    #     squared_engagement = engagements[i] * engagements[i]
    #     squared_engagements.append((squared_engagement, i))

    # squared_engagements.sort(reverse=True)

    # result = [0] * len(engagements)
    # position = len(engagements) - 1

    # for square, original_index in enumerate(squared_engagements):
    #     result[position] = square
    #     position -= 1

    # return result


# A list arranged in none decreasing order means that the largest values are located at the ends when the list contains negative values


def engagement_boost_1(nums):
    start, end = 0, len(nums) - 1

    result = [0] * len(nums)
    pos = len(result) - 1

    while start < end:

        if abs(nums[start]) > nums[end]:
            l_num = (nums[start]) ** 2
            start += 1
        else:
            l_num = nums[end] ** 2
            end -= 1

        result[pos] = l_num
        pos -= 1

    nums[:] = result
    del result
    return nums


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
