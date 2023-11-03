class Solution:
    def parseTernary(self, expression: str) -> str:
        

        stack = []
        expression = expression[::-1]
        for c in expression :
            if len(stack) > 2 and stack[-1] == '?':
                stack.pop()  # Pop '?'
                first = stack.pop()
                stack.pop()  # Pop ':'
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return stack[-1]