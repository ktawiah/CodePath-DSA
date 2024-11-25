import heapq


def merge_lists(lst1, lst2):
    heap1, heap2 = lst1[:], lst2[:]
    heapq.heapify(heap1)
    heapq.heapify(heap2)
    merged = []

    while heap1 and heap2:
        if heap1[0] <= heap2[0]:
            merged.append(heapq.heappop(heap1))

        else:
            merged.append(heapq.heappop(heap2))

    while heap1:
        merged.append(heapq.heappop(heap1))

    while heap2:
        merged.append(heapq.heappop(heap2))

    return merged


print(merge_lists([1, 2, 2, 3], [2, 4, 6]))
