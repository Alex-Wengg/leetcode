class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [n] * n 
        isPalin = [[False] * len(s) for i in range(len(s))]
        
        for i in range(len(s)):
            for j in range(i+1):
                
                if s[i] == s[j] and (i - j < 2 or isPalin[i-1][j+1]):
                    isPalin[i][j] = True
                    if j == 0:
                        cut[i] = 0
                    else:   
                        cut[i] = min(cut[i], cut[j-1] + 1)    
        return cut[-1]