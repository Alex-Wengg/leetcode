class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        cuts = [n] * len(s)  
        cuts[-1] = 0 #

        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j] and ( j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = 1
           
                    cuts[i] = min(cuts[i], cuts[j+1] + 1) if n - 1 != j else 0# shouldn't dp cut check if not mirror
        
        return cuts[0]


 