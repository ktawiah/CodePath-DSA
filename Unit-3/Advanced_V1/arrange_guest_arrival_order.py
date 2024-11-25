"""You are organizing a prestigious event, and you must arrange the ***order in which guests arrive*** based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions."""


def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    stack = []
    guest_order = []

    # We need to assign numbers from 1 to n + 1
    for i in range(n + 1):
        # Push the current number into the stack
        stack.append(i + 1)

        # If we are at the end or we have 'I' in the pattern, we need to pop from the stack
        if i == n or arrival_pattern[i] == "I":
            while stack:
                guest_order.append(str(stack.pop()))

    return "".join(guest_order)


print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))
