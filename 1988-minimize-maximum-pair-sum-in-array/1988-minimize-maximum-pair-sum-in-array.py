class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_ = float('-inf')
        for i in range(len(nums)//2):
            min_ = max(min_, nums[i] + nums[len(nums)-i -1])
        return min_