"""You are given a string schedule representing the lineup of shows on a streaming platform, where each character in the string represents a different show. A duplicate removal consists of choosing two adjacent and equal shows and removing them from the schedule.

We repeatedly make duplicate removals on schedule until no further removals can be made.

Return the final schedule after all such duplicate removals have been made. The answer is guaranteed to be unique."""


def remove_duplicate_shows(schedule):
    stack = []

    for char in schedule:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


print(remove_duplicate_shows("abbaca"))
print(remove_duplicate_shows("azxxzy"))
