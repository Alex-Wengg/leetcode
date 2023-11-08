class Solution:
    def findIntegers(self, n: int) -> int:
        self.s = bin(n)[2:]
        self.n = (len(self.s))
        self.dp = [[[ -1 for i in range(2)] for j in range(2)] for k in range(32)]

        def f(pos, fl, pr):
            if pos == self.n:
                return 1
            if self.dp[pos][fl][pr] != -1:
                return self.dp[pos][fl][pr]
            
            val = 0
            val += f(pos+1, fl | ('0' < self.s[pos]), 0)
            if (not(pr) and (fl == 1 or self.s[pos] == '1')):
                val += f(pos + 1, (fl | ('1' < self.s[pos])), 1)
            self.dp[pos][fl][pr] = val
            return self.dp[pos][fl][pr] 
        
        return f(0, 0, 0)

        