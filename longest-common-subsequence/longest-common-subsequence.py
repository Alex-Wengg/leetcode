class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[ 0 for x in range(len(text1)+1)] for y in range(len(text2)+1)]
        
 
        maxx = 0
        for i in range(1,len(text2)+1):
            for j in range(1, len(text1)+1):
                
                
                part1 = dp[i][j-1]
                part2 = dp[i-1][j]                
                
                if text2[i-1] == text1[j-1]:
                    dp[i][j] += 1 + dp[i-1][j-1]
                else:
                    dp[i][j] += max(part1,part2)
                maxx = max(maxx, dp[i][j])
        return maxx