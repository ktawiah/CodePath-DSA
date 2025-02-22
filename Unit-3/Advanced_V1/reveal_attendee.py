"""You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees. You need to arrange the attendees in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.

The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:

Take the top registration number from the list, reveal it, and remove it from the list.
If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
Return an ordering of the registration numbers that would reveal the attendees in increasing order."""

from collections import deque


def reveal_attendee_list_in_order(attendees):
    # Create a queue of attendees to simulate process
    queue = deque(attendees)

    # Create a list to store the revealed attendees
    revealed = []

    while queue:

        # Remove, and reveal top attendee
        revealed.append(queue.popleft())

        # Move next attendee to the bottom
        if queue:
            queue.append(queue.popleft())

    #  Return revealed attendees
    return revealed


print(reveal_attendee_list_in_order([17, 13, 11, 2, 3, 5, 7]))
print(reveal_attendee_list_in_order([1, 1000]))

[17, 11, 3, 7, 2, 13, 5]
[1, 1000]
