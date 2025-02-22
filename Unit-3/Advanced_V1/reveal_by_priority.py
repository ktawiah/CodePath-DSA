"""You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

Your task is to rearrange the attendees list such that the following conditions are met:

Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
Return the attendees list after the rearrangement."""


def arrange_attendees_by_priority(attendees, priority):
    # Create three lists to store priorities
    less, middle, greater = [], [], []

    # Iterate through attendees list
    for attendee in attendees:

        # Update either lists based on priority
        if attendee < priority:
            less.append(attendee)
        elif attendee == priority:
            middle.append(attendee)
        else:
            greater.append(attendee)

    # Return concatenated list
    return less + middle + greater


print(arrange_attendees_by_priority([9, 12, 5, 10, 14, 3, 10], 10))
print(arrange_attendees_by_priority([-3, 4, 3, 2], 2))

[9, 5, 3, 10, 10, 12, 14]
[-3, 2, 4, 3]
