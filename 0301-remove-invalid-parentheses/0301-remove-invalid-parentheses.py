class Solution:
    def removeInvalidParentheses(self, s):


        def isValided(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                if c == ')':
                    if count > 0:
                        count -= 1
                    else:
                        return False
            return count == 0

        q = []
        q.append((s, 0))
        res = []
        while q:
            ss, position = q.pop(0)

            if(isValided(ss)):
                res.append(ss)
            elif not res:
                for i in range(position, len(ss)):
                    if ss[i] in {'(',')'} and (i == position or ss[i]!=ss[i-1]):
                        q.append((ss[0:i] + ss[i+1:], i))
        return res
