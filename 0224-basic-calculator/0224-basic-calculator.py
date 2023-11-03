class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign = 1
        result = 0
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                number = 10 * number + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.extend([ result, sign ])
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number 
                number = 0
                result *= stack.pop()
                result += stack.pop()
            
        if number != 0:
            result += sign * number 
        return result