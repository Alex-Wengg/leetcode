class Solution:
    def maxScore(self, s: str) -> int:
        cnt = 0 
        if len(s) <= 2:
            return s[0].count('0')+ s[1].count('1')
        for i in range(1, len(s)):
            cnt = max(cnt, s[:i].count('0') + s[i:].count('1'))
        return cnt