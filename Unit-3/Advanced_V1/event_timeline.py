"""You are given two strings event and timeline. Initially, there is a string t of length timeline.length with all t[i] == '?'.

In one turn, you can place event over t and replace every letter in t with the corresponding letter from event.

For example, if event = "abc" and timeline = "abcba", then t is "?????" initially. In one turn, you can:

place event at index 0 of t to obtain "abc??",
place event at index 1 of t to obtain "?abc?", or
place event at index 2 of t to obtain "??abc".
Note that event must be fully contained within the boundaries of t in order to mark (i.e., you cannot place event at index 3 of t). We want to convert t to timeline using at most 10 * timeline.length turns.

Return an array of the index of the left-most letter being marked at each turn. If we cannot obtain timeline from t within 10 * timeline.length turns, return an empty array.
"""


def mark_event_timeline(event, timeline):
    pass


print(mark_event_timeline("abc", "ababc"))
print(mark_event_timeline("abca", "aabcaca"))

[0, 2]
[3, 0, 1]
