class Solution:
    def findTargetSumWays(self, nums, s):
        summ = 0
        for i in nums:
            summ +=i
        
        if (s > summ or s< -summ):
            return 0 
        
        dp = []
        for i in range(2*summ+1):
            dp.append(0) 
        dp[0+summ] = 1;
        
        
        for i in range(len(nums)):
            nextt = []
            for x in range(2*summ+1):
                nextt.append(int(0)) 

            for k in range(2*summ+1):
                
                if (dp[k] != 0):
                    nextt[k + nums[i]] += dp[k]
                    nextt[k - nums[i]] += dp[k]
            dp = nextt
        
        return dp[summ+s]