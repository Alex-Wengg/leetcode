class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # input: s string to examine
        # input: t string candidate
        # a solution using DP and bottom up may fit
        ''' 
               b a b g b a g  
              1 1 1 1 1 1 1 1
            b 0 1 1 2 2 3 3 3
            a 0 0 1 1 1 1 4 4
            g 0 0 0 0 1 1 1 5 
            if t[i] == s[j] match 
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]        
        '''
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]

        
        # empty substring is always part of a string but once
        for i in range(len(t)+1):
            dp[i][0] = 0
        # non empty substring in empty string is 0
        for j  in range(len(s)+1):
            dp[0][j] = 1
        
        for i in range(1, len(t)+1):
            
            for j in range(1, len(s)+1):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[-1][-1]