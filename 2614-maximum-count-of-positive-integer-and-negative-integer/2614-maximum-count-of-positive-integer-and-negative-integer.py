class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        min_ = 0
        max_ = 0
        for num in nums:
            min_ += num < 0
            max_ += num > 0

        return max(min_, max_) 