"""
You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing the guests you have at the music festival. Each character in guests is a type of guest you have. You want to know how many of the guests you have are also VIP pass holders.

Letters are case sensitive, so "a" is considered a different type of guest from "A".

Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.
"""


def num_VIP_guests(vip_passes, guests):
    # Create counter to store passes count
    count = 0

    # Create as set of vip passes
    vip_passes_set = set(vip_passes)

    # Iterate through guests
    for guest in guests:

        # Check if guest has VIP pass and update count
        if guest in vip_passes_set:
            count += 1

    # Return count
    return count


vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
