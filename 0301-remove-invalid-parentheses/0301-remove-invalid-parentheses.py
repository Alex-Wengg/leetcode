class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        if not s:
            return res

        visited = set()
        queue = []

        visited.add(s)
        queue.append(s)

        found = False

        def isValided(s):
            count = 0
            for i in range(len(s)):
                if s[i] == '(':
                    count += 1
                if s[i] == ')' and count == 0:
                    return False
                elif s[i] == ')':
                    count -= 1
            return count == 0 

        while queue:
            s = queue.pop(0)
            if isValided(s):
                found = True
                res.append(s)
            if found:
                continue
            
            for i in range(len(s)):
                if s[i] not in {'(',')'}:
                    continue
                t = s[0:i] + s[i+1:]
                if t not in visited:
                    queue.append(t)
                    visited.add(t)
            
        return res