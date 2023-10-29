class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        sum_ = 0

        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                sum_ += n
        return sum_