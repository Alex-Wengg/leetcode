class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        # when to drop, if dropping makes it bigger
        # when to append, if makes it bigger
        min_ = 0
        max_ = 0
        result = 0

        for n in nums:
            min_ = min(0, min_ + n)
            max_ = max(0, max_ + n)
            result = max(result, -min_, max_)
        return result