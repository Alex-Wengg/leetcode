class Solution:
    def popcount(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt

    def minFlips(self, a: int, b: int, c: int) -> int:
        return self.popcount((a | b) ^ c) + self.popcount(a & b & ~c)