class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def longestPalindrome(s):
            T = '#'.join('^{}$'.format(s))
            n = len(T)
            P = [0] * n 
            C, R = 0, 0 

            for i in range(1, n - 1):
                P[i] = (R > i) and min(R - i, P[2*C - i])
                
                while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                    P[i] += 1
                
                if i + P[i] > R:
                    C = i 
                    R = i + P[i]
                
            return max(P)
        
        for word in words:
            if longestPalindrome(word) == len(word):
                return word 
        return ""