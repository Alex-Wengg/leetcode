class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [ [0] * n for i in range(n)]

        for i in range( n -2 , -1 , -1):
            for j in range(i + 2, n):
                max_coins = 0
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    max_coins = max(max_coins, coins)
                dp[i][j] = max_coins
        return dp[0][n-1]