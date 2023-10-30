class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_ = []
        max_ = []

        diff_i = 0
        min_diff = float("inf")
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) < min_diff:
                diff_i = i
                min_diff = nums[i] - nums[i-1]
        return min_diff