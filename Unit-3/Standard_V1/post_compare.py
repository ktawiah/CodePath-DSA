"""You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty."""


def convert_draft(draft):
    stack = []

    for char in draft:
        if char != "#":
            stack.append(char)
        elif stack:
            stack.pop()

    return "".join(stack)


def post_compare(draft1, draft2):
    return convert_draft(draft1) == convert_draft(draft2)


print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#"))
print(post_compare("a#c", "b"))
