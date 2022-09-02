class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [-1] + [n] * n 
        isPalin = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (j+1>=i or isPalin[i-1][j+1]):
                    isPalin[i][j] = True
                    cut[i+1] = min(cut[i+1], cut[j]+1)
                    
        return cut[-1]