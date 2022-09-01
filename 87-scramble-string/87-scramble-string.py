class Solution:
    def isScramble(self, s1, s2):
    
        def scramble( s1, s2):
            n, m = len(s1), len(s2)
            if  sorted(s1) != sorted(s2):
                return False
            if s1 == s2:
                return True
            f = scramble
            if (s1, s2) in dp:
                return dp[(s1,s2)]
            dp[(s1,s2)] = False
            for i in range(1, n):
                # simulate the string splitting
                if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or\
                f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                    dp[(s1, s2)] = True
                    return True
            return dp[(s1,s2)]
        dp = dict()


        return scramble(s1,s2)