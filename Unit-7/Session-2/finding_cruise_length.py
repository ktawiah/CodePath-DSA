"""It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise."""


def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
