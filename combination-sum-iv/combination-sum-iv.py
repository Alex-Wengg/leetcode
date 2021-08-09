class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (1+target)
        for num in nums:
            if num <= target:
                dp[num] = 1
        
        for i in range(1,target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
            print(dp)
        
        return dp[-1]