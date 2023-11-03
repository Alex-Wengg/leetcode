class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0

        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                pre_i = stack.pop()
                if not(stack):
                    stack.append(i)
                res = max(res, i - stack[-1])
                
        return res 

 