class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        row = len(matrix)
        col = len(matrix[-1])
        
        dp = [[0] * col for _ in range(row)]     
        maxLength = 0
        for i in range(row):
            for j in range(col):
                if i - 1 < 0 or j - 1 < 0:
                    if matrix[i][j] == '1': dp[i][j] = 1
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                maxLength = max(maxLength, dp[i][j])
        print(dp)
    
        return maxLength*maxLength
                