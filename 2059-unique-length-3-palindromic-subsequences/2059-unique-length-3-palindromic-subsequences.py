class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen_ = set()
        cnt = 0

        for c in string.ascii_lowercase:
            i = s.find(c)
            j = s.rfind(c)
            if i > -1:
                cnt += len(set(s[i+1:j]))
        return cnt