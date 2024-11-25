"""You are managing a watchlist for a streaming service, represented by a string watchlist consisting of lowercase English letters, where each letter represents a different show.

You are allowed to perform operations on this watchlist. In one operation, you can replace a show in watchlist with another show (i.e., another lowercase English letter).

Your task is to make the watchlist a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

Return the resulting watchlist string.

Implement the following pseudocode:

1. Convert the watchlist string to a list.
2. Initialize two pointers:
   * Left Pointer: Start at the beginning of the list (index 0).
   * Right Pointer: Start at the end of the list (last index).
3. While the left pointer is less than the right pointer:
   a. Compare the characters at the left and right pointers.
   b. If the characters are different:
      * Replace the character that is alphabetically later (greater) with the one that is earlier (smaller) to make the string lexicographically smaller.
   c. Move the left pointer one step to the right.
   d. Move the right pointer one step to the left.
4. Convert the list back to a string.
5. Return the resulting string."""


def make_smallest_watchlist(watchlist):
    """
    P: Converting watchlist string into a palindrome in the smallest number of ways and returning the lexicographically smaller string.
    T.C: 0(n)
    S.C: 0(n)
    """

    # Convert watchlist to a list
    watch_list = list(watchlist)

    # Create pointers
    start, end = 0, len(watch_list) - 1

    # If equal -> move both pointers
    while start < end:
        if watch_list[start] != watch_list[end]:
            if ord(watch_list[start]) > ord(watch_list[end]):
                watch_list[start] = watch_list[end]
            else:
                watch_list[end] = watch_list[start]

        start += 1
        end -= 1

    return "".join(watch_list)

    # If not equal -> replace diff char with char of min ord -> move pointers

    # Return string form of watchlist


print(make_smallest_watchlist("egcfe"))
print(make_smallest_watchlist("abcd"))
print(make_smallest_watchlist("seven"))
