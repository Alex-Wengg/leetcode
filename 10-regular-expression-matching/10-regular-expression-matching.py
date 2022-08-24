class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # we are gonna do this using dp bottom up 
        # its not gonna be difficult but the * will be the bigg consideration
        # we will need to cover when x*, has no x, 1 x, >1 x
        # . and matching string & pattern, we can use dp[i-1][j-1]
    
        dp =[ [False] * (len(s)+1) for j in range(len(p)+1)]
        dp[0][0] = True
        for i in range(2, len(p)):
            dp[i][0] = dp[i-2][0] and p[i-1] =='*'
        for i in range(1, len(p)+1):
            
            for j in range(1, len(s)+1):
                
               
                
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    dp[i][j] = dp[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]
        return dp[-1][-1]