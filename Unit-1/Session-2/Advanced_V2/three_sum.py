"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def three_sum(nums):
    results = []
    nums.sort()  # Sort the array for two-pointer technique

    for index, num in enumerate(nums):
        # Skip duplicates
        if index > 0 and num == nums[index - 1]:
            continue

        # Use two pointers to find the remaining two numbers
        start = index + 1
        end = len(nums) - 1

        while start < end:
            new_sum = num + nums[start] + nums[end]
            if new_sum == 0:
                results.append([num, nums[start], nums[end]])
                start += 1
                end -= 1

                # Skip duplicates for start and end
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif new_sum < 0:
                start += 1
            else:
                end -= 1

    return results

    #     fin_result = []


#     # Step 2: Loop through each number in the array
#     for num_idx, num in enumerate(nums):
#         # Skip duplicate values for the first element
#         if num_idx > 0 and num == nums[num_idx - 1]:
#             continue

#         diff_map = {}

#         # Step 3: Find pairs that sum up to -num
#         for j in range(num_idx + 1, len(nums)):  # Start from the next element
#             complement = -num - nums[j]

#             if nums[j] in diff_map:
#                 # Found a triplet: num, nums[j], and complement (stored in diff_map)
#                 fin_result.append([num, complement, nums[j]])

#                 # Skip duplicates for the second element
#                 while j + 1 < len(nums) and nums[j] == nums[j + 1]:
#                     j += 1
#             else:
#                 # Add the current number to the diff_map
#                 diff_map[complement] = j

#     return fin_result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))
