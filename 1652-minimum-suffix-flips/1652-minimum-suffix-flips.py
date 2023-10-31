class Solution:
    def minFlips(self, target: str) -> int:

        flip = '0'
        cnt = 0

        for c in target:
            if flip != c:
                cnt += 1
                flip = c
        return cnt