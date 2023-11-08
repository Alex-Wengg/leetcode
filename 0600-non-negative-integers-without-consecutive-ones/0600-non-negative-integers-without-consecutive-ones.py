# The user has provided a top-down (recursive with memoization) approach and is asking for a bottom-up (iterative) approach.
# We need to rewrite the provided recursive function as an iterative one.

class Solution:
    def findIntegers(self, n: int) -> int:
        # Convert number to binary and store it
        self.s = bin(n)[2:]
        self.n = len(self.s)
        
        # Initialize dp table
        self.dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(self.n + 1)]
        
        # Base case: If we haven't placed any digits yet, there is 1 way to place nothing
        for fl in range(2):
            for pr in range(2):
                self.dp[self.n][fl][pr] = 1
        
        # Fill dp table iteratively (bottom-up)
        for pos in range(self.n - 1, -1, -1):
            for fl in range(2):
                for pr in range(2):
                    self.dp[pos][fl][pr] += self.dp[pos + 1][fl | ('0' < self.s[pos])][0]
                    
                    if not pr and (fl == 1 or self.s[pos] == '1'):
                        self.dp[pos][fl][pr] += self.dp[pos + 1][fl | ('1' < self.s[pos])][1]
        
        return self.dp[0][0][0]
