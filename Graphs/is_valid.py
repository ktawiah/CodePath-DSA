def is_valid_post_format(posts):
    stack = []
    brack_dict = {"}": "{", ")": "(", "]": "["}

    for char in posts:
        if char in {"{", "[", "("}:
            stack.append(char)
        elif brack_dict.get(char) == stack[-1]:
            stack.pop()

        # print(stack)

    return len(stack) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
