class Solution:
    def minCut(self, s: str) -> int:
        
        pal = [[True] * len(s) for _ in range(len(s))]
        cut = [0] * len(s)
   
        minCut = 0
        
        for i in reversed(range(0, len(s))):
            minCut = float('inf')
            for j in range(i, len(s)):
                pal[i][j] = s[i] == s[j] and ( j - i < 3 or pal[i+1][j-1])
                if pal[i][j]:                        
                    minCut = min(minCut, cut[j+1] + 1 if len(s) - 1 > j else 0)

            cut[i] = minCut

        return cut[0]