class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # n is the max # of cuts to make palindrome
        cut = [-1] + [n] * n 
        isPalin = [[False] * len(s) for i in range(len(s))]
        
        for i in range(len(s)):
            
            for j in range(i+1):
                                    # check if aa or a 
                if s[i] == s[j] and (i - j <= 1 or isPalin[i-1][j+1]):
                    isPalin[i][j] = True
                    # j=0 means starting one char and the # of cuts for one char is 0
                    cut[i+1] = min(cut[i+1], cut[j] + 1)    
     
        return cut[-1]