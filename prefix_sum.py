def subarraySum(nums, k: int):
    prefix_sum, prefix_map, subarrays = 0, {0: [-1]}, []
    max_len = float("-inf")

    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            for start_index in prefix_map[prefix_sum - k]:
                subarrays.append(nums[start_index + 1 : i + 1])
                max_len = max(max_len, i - start_index + 1)
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, []) + [i]

    return max_len, print(subarrays)


# print(subarraySum([15, -2, 2, -8, 1, 7, 10, 23], 0))


class Solution:
    def maxLen(self, arr):
        # Create prefix map, sum
        prefix_map, prefix_sum = {0: [-1]}, 0

        # Create placholder for array
        result = []

        # Iterate through nums
        for i, num in enumerate(arr):

            # Update prefix sum
            prefix_sum += num

            # Update max array if curr arr len greater than that of max array
            if prefix_sum in prefix_map:
                for start in prefix_map.get(prefix_sum, []):
                    curr = arr[start + 1 : i + 1]
                    if len(curr) > len(result):
                        result = curr

            # Update prefix map
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, []) + [i]

        return result


print(Solution().maxLen([15, -2, 2, -8, 1, 7, 10, 23]))
