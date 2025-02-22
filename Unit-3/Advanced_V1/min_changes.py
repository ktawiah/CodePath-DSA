"""You are organizing a series of events, and each event is represented by a parenthesis in the string schedule, where an opening parenthesis ( represents the start of an event, and a closing parenthesis ) represents the end of an event. A balanced schedule means every event that starts has a corresponding end.

However, due to some scheduling issues, the current schedule might not be balanced. In one move, you can insert either a start or an end at any position in the schedule.

Return the minimum number of moves required to make the schedule balanced."""


def min_changes_to_make_balanced(schedule):
    # Create a stack to balance brackets
    stack = []

    # Create counter for deviations
    deviations = 0

    # Iterate through schedule
    for par in schedule:
        if par == ")":
            if stack:
                stack.pop()
            # Update counter if anomaly
            else:
                deviations += 1
        else:
            stack.append(par)

    # Return len of stack if counter == 0 else return counter
    return deviations if deviations else len(stack)


print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("((("))

1
3
