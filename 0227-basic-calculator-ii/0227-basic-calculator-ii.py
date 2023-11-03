class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "-+*/" or (  i == len(s) - 1):

                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)