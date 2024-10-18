"""
Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.

Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

You don't need to modify intervals in-place. You can make a new array and return it.
"""


def insert_interval(intervals, new_interval):
    # Insert new interval into original intervals list
    index = 0

    while index < len(intervals) - 1:
        if intervals[index][0] <= new_interval[0] <= intervals[index + 1][0]:
            intervals.insert(index + 1, new_interval)
            break

        index += 1

    # Merge interval
    stack = [intervals[0]]

    for interval in intervals:
        top_interval = stack[-1]

        if interval[0] < top_interval[1]:
            top_interval[1] = interval[1]
        else:
            stack.append(interval)

    print(stack)


intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)
