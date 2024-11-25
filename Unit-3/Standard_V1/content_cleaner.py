"""You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean."""


def clean_post_alt(post):
    # Create a stack
    stack = []

    # Iterate through the post
    for char in post:

        # Check if alternate is in stack and stack not empty
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

    # Return string of stack


def clean_post(post):
    # Convert post to a list
    post_list = list(post)

    # Iterate to last but one
    start = 0
    while start < len(post_list) - 1:
        if (
            post_list[start].lower() == post_list[start + 1].lower()
            and post_list[start] != post_list[start + 1]
        ):
            post_list.pop(start)
            post_list.pop(start)
            if start > 0:
                start -= 1
        else:
            start += 1

    # Return result string
    return "".join(post_list)


print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))
