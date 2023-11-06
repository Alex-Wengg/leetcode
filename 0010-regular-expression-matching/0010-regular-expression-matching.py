class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [ [0 for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = 1
        for j in range(1, len(p)+1):
            dp[0][j] = p[ j - 1 ] == '*' and dp[0][j-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in [s[i-1], "."]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (p[j-2] in [s[i-1], '.'] and dp[i-1][j])
        return dp[-1][-1]