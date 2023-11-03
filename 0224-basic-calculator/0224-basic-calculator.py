class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        stack = []
        sign = 1 #
        res = 0 # using res to cache past result for () encounters

        for i, c in enumerate(s): 
            if c.isdigit(): # 
                number = number * 10 + int(c)  # 
            elif c in '-+)':
                res += number * sign # 
                number = 0
                if c in '-+':
                    sign = 1 if c == '+' else -1
                elif c == ')':
                    res *= stack.pop()
                    res += stack.pop()
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1 #
                res = 0 #
            
        if number != 0:
            res += sign * number
        return res
