class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPalindrome = [[False] * len(s) for _ in range(len(s))]
        cut = [-1] + [len(s)] * len(s)

        for i in range(len(s)):
            
            for j in range(i+1):
                if s[i]==s[j] and ( i-j<2 or isPalindrome[i-1][j+1]):
                    isPalindrome[i][j] = True
                    #failed bc you need to track cut[i+1] prior subProblem solved
                    #we check j to see if its past sequence worked before
                    # cut[i+1] = min(cut[i], cut[i]+1)
                    cut[i+1] = min(cut[i+1], cut[j]+1)
                    
        return cut[-1]