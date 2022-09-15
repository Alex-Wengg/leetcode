class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        
        max_buy = 0
        n = len(prices)
        if k >= n / 2:
            for i in range(1, n):
                max_buy += max(prices[i] - prices[i-1], 0)
            return max_buy
        
        dp_sell = [ [0] * n for i in range(k+1)]
        
        for i in range(1,k+1):
            # mini buy to initialize the dp
            max_profitFromBuy = -prices[0]
            for j in range(1, n):
                dp_sell[i][j] = max(dp_sell[i][j-1], prices[j]+max_profitFromBuy)
                max_profitFromBuy = max(max_profitFromBuy, -prices[j] + dp_sell[i-1][j])
        return dp_sell[-1][-1]
            