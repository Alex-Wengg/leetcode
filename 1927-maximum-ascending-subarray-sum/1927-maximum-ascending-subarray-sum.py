class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        sum_ = nums[0]
        max_ = 0
        if len(nums) == 1:
            return nums[0]
            
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sum_ += nums[i]
            else: 
                max_ = max(max_, sum_ )
                sum_ = nums[i]
            
            max_ = max(max_, sum_ )
        return max_