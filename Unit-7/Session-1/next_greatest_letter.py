def next_greatest_letter(letters, target):
    start, end = 0, len(letters)-1

    while start < end:
        mid = (start + end) // 2
        if ord(letters[mid]) >= ord(target):
            if letters[mid-1] and ord(letters[mid-1]) > ord(target):
                end = mid-1
            else:
                return letters[mid]
        else:
            start = mid + 1

    return letters[0]

print(next_greatest_letter(["c", "f", "j"], "a"))
print(next_greatest_letter(["x", "x", "y", "y"], "z"))

