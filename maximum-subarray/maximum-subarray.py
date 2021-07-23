class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result =  nums[0]
        windowSum, windowStart =  nums[0],  nums[0]
        for windowEnd in range(1, len(nums)):
            windowSum += nums[windowEnd]
            windowSum = max(windowSum,  nums[windowEnd])
            result = max(result, windowSum )
            
        return result