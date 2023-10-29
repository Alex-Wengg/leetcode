class Solution:
    def isArmstrong(self, n: int) -> bool:
        len_ = len(str(n))
        return n == sum([int(d) ** len_ for d in str(n)])