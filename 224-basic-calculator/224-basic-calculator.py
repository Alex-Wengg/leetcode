class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            
            elif char in ['-', '+']:
                res += sign*num
                num = 0
                sign = [-1,1][char=='+']
            
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            
            elif char == ')':
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        
        return res + num*sign