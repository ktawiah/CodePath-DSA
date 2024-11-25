import heapq


def k_max(nums, k):
    if k == 0:
        return []

    # Create a min-heap of size k
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Iterate through the rest of the elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(
                min_heap, num
            )  # Pop the smallest and push the new element

    return min_heap  # Return the sorted result in descending order


# def k_max(nums, k):
#     result = []
#     heapq._heapify_max(nums)
#     while k != 0:
#         result.append(nums.pop(0))
#         heapq._heapify_max(nums)
#         k -= 1
#     return result


print(k_max([9, 3, 7, 1, -2, 6, 8], 2))
