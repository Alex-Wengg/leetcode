class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1

        maxLength = 1
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                #if > nums 
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
                    maxLength = max(maxLength, dp[i])
        return maxLength