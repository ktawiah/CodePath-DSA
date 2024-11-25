"""You want to add a creative twist to your posts by reversing the order of characters in each word within your post while still preserving whitespace and the initial word order. Given a string post, use a queue to reverse the order of characters in each word within the sentence."""


def reverse_str(str_input):
    start, end = 0, len(str_input) - 1

    str_lst = list(str_input)

    while start < end:
        str_lst[start], str_lst[end] = str_lst[end], str_lst[start]
        start += 1
        end -= 1

    return "".join(str_lst)


def edit_post(post):
    post_list = post.split()
    result = [0] * len(post_list)
    curr_idx = len(result) - 1

    while post_list:
        result[curr_idx] = reverse_str(post_list.pop())
        curr_idx -= 1

    return " ".join(result)


print(edit_post("Boost your engagement with these tips"))
print(edit_post("Check out my latest vlog"))
