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

        q = [s]
        ht = set( )
        
        res = []

        while q:
            ss = q.pop(0)
            
            # skippers
            if ss in ht:
                continue
            ht.add(ss)
            
            # checkers 
            if isValided(ss):
                res.append(ss)
            elif not res:

                for i in range(len(ss)):
                    if ss[i] in {'(',')'}:
                        q.append(ss[0:i] + ss[i+1:])
        return res