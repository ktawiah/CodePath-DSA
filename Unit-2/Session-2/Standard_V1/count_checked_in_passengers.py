"""As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.

Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.
"""

# def count_checked_in_passengers(rooms, start=0, count=0):
#     if start == len(rooms):
#         return count

#     if rooms[start] == 1:
#         count += 1

#     return count_checked_in_passengers(rooms, start + 1, count)


def count_checked_in_passengers(rooms, curr=None, count=0):
    if len(rooms) == 0:
        return -1

    curr = rooms.pop()

    if curr == 1:
        count += 1

    return count_checked_in_passengers(rooms, curr=curr, count=0)


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1))
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
