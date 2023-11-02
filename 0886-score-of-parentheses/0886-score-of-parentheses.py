class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cnt = 0

        for c in s:
            if c == '(':
                stack.append(cnt)
                cnt = 0
            else:
                cnt += stack.pop() + max(cnt, 1)
        return cnt
            
