"""You are organizing an event, and you have a 0-indexed list guests of even length, where each element represents either an attendee (positive integers) or an absence (negative integers). The list contains an equal number of attendees and absences.

You should return the guests list rearranged to satisfy the following conditions:

Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
For all elements with the same sign, the order in which they appear in the original list must be preserved.
The rearranged list must begin with an attendee (positive integer).
Return the rearranged list after organizing the guests according to the conditions."""


def rearrange_guests(guests):
    """
    P: Arrange guests in alternative order of signs
    """

    # Create a list for positive and negative vals
    pos_vals, neg_vals = [], []

    # Iterate through guests and update lists
    for guest in guests:
        if guest < 0:
            neg_vals.append(guest)
        else:
            pos_vals.append(guest)

    # Create a result list
    result = []

    # Create a pointer and update result list alternatively
    start = 0

    while start < len(pos_vals):
        result.append(pos_vals[start])
        result.append(neg_vals[start])
        start += 1

    # Return result list
    return result


print(rearrange_guests([3, 1, -2, -5, 2, -4]))
print(rearrange_guests([-1, 1]))
