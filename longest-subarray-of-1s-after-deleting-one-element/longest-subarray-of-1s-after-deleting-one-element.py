class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        new, old, m = 0, 0, 0
        for num in nums:
            if num == 1:
                old, new = old + 1, new + 1
            else:
                old, new = new, 0
            m = max(m, old)
        return min(m, len(nums) - 1)
    