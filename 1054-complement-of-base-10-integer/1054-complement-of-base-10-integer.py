class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        for i in range(1, 32):
            max_ = 2 ** i
            if max_ > n:
                return max_ - n -1
        return -1