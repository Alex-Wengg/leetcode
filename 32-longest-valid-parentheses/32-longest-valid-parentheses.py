class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxx = 0
        
        stack = []
        stack.append(-1)
        
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if len(stack) == 0:
                    stack.append(i)
                else:
                    print(stack[-1])
                    maxx = max(maxx, i - stack[-1])
        return maxx