class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res  = 0 
        cnt = 0

        for c in s:
            cnt += 1 if 'L' == c else -1
            if cnt == 0:
                res += 1
        return res