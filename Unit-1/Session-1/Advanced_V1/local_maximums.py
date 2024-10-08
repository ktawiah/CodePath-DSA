def local_maximums(input):
    """
    1. Create placeholder for maximums
    2. Loop through matrix
    3. Update value in new matrix for max value

    """
    output = []
    # dict_count = {}

    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            continue
        else:
            output.append(input[i])
            i += 1

    return "".join(output)
    # for char in input:
    #     dict_count[char] = dict_count.get(char, 0) + 1

    # for char, count in dict_count.items():
    #     if count == 1:
    #         output.append(char)

    # return "".join(output)


print(local_maximums("azxxzy"))
print(local_maximums("abbaca"))
