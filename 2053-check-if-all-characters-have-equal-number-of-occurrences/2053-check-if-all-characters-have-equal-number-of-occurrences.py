class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = collections.Counter(s)
        print(c.values())
        return len(set(c.values())) == 1