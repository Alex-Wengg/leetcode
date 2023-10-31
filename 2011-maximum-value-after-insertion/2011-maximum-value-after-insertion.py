class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        if '-' in n:
            for i, c in enumerate(n):
                if c.isdigit() and int(c) > x:
                    str_ = str(n[:i] + str(x) + n[i:])
                    return str_
        else:
            for i, c in enumerate(n):
                if int(c) < x:
                    str_ = str(n[:i] + str(x) + n[i:])
                    return str_
        str_ = str(n + str(x)  )
        return str_