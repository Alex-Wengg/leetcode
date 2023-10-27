from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        if len(text) < len("balloon"):
            return 0
        cntBalloon = Counter("balloon")

        cnt = Counter(text)

        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])
