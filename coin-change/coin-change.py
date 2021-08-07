class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [ [math.inf for _ in range(amount+1)] for _ in range(len(coins))]

        #vertical
        for i in range(len(coins)):
            dp[i][0] = 0
        #the coins
        for i in range( len(coins)):
            #sums with the coins
            for j in range(1,amount+1):
                if i > 0:
                    dp[i][j] = dp[i-1][j]
                
                if j >=  coins[i] :
                    if dp[i][j-coins[i]] != math.inf:
                        dp[i][j] =min(dp[i][j], dp[i][j-coins[i]]+1)

        return -1 if dp[len(coins) - 1][amount] == math.inf  else dp[len(coins) - 1][amount]