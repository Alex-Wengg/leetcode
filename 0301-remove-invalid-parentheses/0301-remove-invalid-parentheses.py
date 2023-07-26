class Solution:
    def removeInvalidParentheses(self, s):
        ans =[]
        def remove(s, ans, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    stack += 1
                if s[i] == par[1]:
                    stack -= 1
                if stack >= 0:
                    continue 

                for j in range(last_j, i+1):
                    if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                        remove(s[0:j] + s[j+1: len(s)], ans, i,j, par )
                return 
            reversed = s[::-1]
            if par[0] == '(':
                remove(reversed, ans, 0,0, [')', '('])
            else:
                ans.append(reversed)
                
        remove(s, ans, 0, 0, ['(',')'])
        return ans

    