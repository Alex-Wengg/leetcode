class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [float("inf")] * (n+1)
        dp[n-1] = 1
        # for i in reversed(range(n)):
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
            # for j in reversed(range(n)):
                dp[j] = max(1, (min(dp[j+1], dp[j])-dungeon[i][j]))
        
        return dp[0]