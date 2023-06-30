class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        dp = [[0 for i in range(len(prices))] for j in range(3)]

        maxBuys = 0 

        for i in range(1, 3):
            currMaxProfit = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], currMaxProfit + prices[j])
                currMaxProfit = max(currMaxProfit, dp[i-1][j] - prices[j],dp[i][j] - prices[j] )
        for i in dp:
            print(i)
        return dp[-1][-1]