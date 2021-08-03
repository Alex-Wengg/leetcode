class Solution:
    def canPartition(self, nums):
        summ = sum(nums) 
        if summ % 2 != 0:
            return False
        return self.helper(summ//2, nums)
    def helper(self,summ, nums):
        
        dp = [[False for i in range(summ+1)] for j in range(len(nums))]
                
        for i in range(len(nums)):
            dp[i][0] = True
        for j in range(1, summ+1):
            dp[0][j] = nums[0] == j
            
        for i in range(len(nums)):
            for j in range(summ+1):
                
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j > nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]]
                    
        return dp[len(nums)-1][summ]