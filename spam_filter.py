from typing import List


class Solution:
    def getSpamComments(
        self, comments: List[str], spam_keywords: List[str]
    ) -> List[str]:

        pass


spam_keyword1 = ["bright", "bonanza", "paid"]
comment1 = ["The sun is bright", "Blockbuster bonanza"]
# ["not_spam", "not_spam"]
spam_keyword2 = ""
comment2 = ""

print(Solution().getSpamComments(spam_keyword1, comment1))
print(Solution().getSpamComments(spam_keyword2, comment2))
