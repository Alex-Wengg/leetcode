class Solution:
    def isScramble(self, s1, s2):
    
        def scramble( s1, s2):
            n, m = len(s1), len(s2)
            if n != m or sorted(s1) != sorted(s2):
                return False
            if s1 == s2:
                return True
            f = scramble
            if (s1, s2) in dp:
                return dp[(s1,s2)]
            dp[(s1,s2)] = False
            for i in range(1, n):
                if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]):
                    dp[(s1, s2)] = True
                    return True
                if f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                    dp[(s1, s2)] = True
                    return True
            return dp[(s1,s2)]
        dp = dict()
        return scramble(s1,s2)