"""You have a watchlist consisting only of uppercase English letters representing movies. Each movie is represented by a unique letter.

You can apply some operations to this watchlist where, in one operation, you can remove any occurrence of one of the movie pairs "AB" or "CD" from the watchlist.

Return the minimum possible length of the modified watchlist that you can obtain.

Note that the watchlist concatenates after removing the movie pair and could produce new "AB" or "CD" pairs."""


def min_remaining_watchlist(watchlist):
    if len(watchlist) <= 1:
        return len(watchlist)

    stack = []

    for char in watchlist:
        if stack and ((stack[-1] + char == "AB") or (stack[-1] + char == "CD")):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


print(min_remaining_watchlist("ABFCACDB"))
print(min_remaining_watchlist("ACBBD"))
