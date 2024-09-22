def reverse(sentence_list):
    start = 0
    end = len(sentence_list) - 1

    while start < end:
        sentence_list[start], sentence_list[end] = (
            sentence_list[end],
            sentence_list[start],
        )
        start += 1
        end -= 1

    return sentence_list


def reverse_sentence(sentence):
    """
    P: Reverse the words in a sentence

    'This is me' -> 'me is This'
    'me' -> 'me'

    S: 1. Create a placeholder for sentence_list, split sentence into a list, and assign to place holder
    'This is me' ['This', 'is', 'me']
    2. Reverse list
       - Create pointers for start and end indices
       - Swap values of indices
       - Decrement end and increment start indices resp.
       - Stop when start >= stop

    3. Join reverse list to a new string using .join()
    """
    sentence_list = sentence.split()
    reversed_list = reverse(sentence_list)
    return " ".join(reversed_list)


if __name__ == "__main__":
    print(reverse_sentence("tubby little cubby all stuffed with fluff"))
    print(reverse_sentence("Pooh"))
