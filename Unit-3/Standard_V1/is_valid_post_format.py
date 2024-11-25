"""You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order."""


def is_valid_post_format(posts):
    if len(posts) <= 1:
        return False

    bracket_map = {")": "(", "}": "{", "]": "["}

    opening_set = set(bracket_map.values())

    stack = []

    for char in posts:
        if char in opening_set:
            stack.append(char)
        else:
            if stack and bracket_map.get(char) == stack[-1]:
                stack.pop()
            else:
                return False

    return not stack


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
