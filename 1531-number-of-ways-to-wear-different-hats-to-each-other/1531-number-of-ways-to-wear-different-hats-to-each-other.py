class Solution:
    def numberWays(self, p2h: List[List[int]]) -> int:

        h2p = [ [] for i in range(40)] # 40^10 faster > 10^40
        n = len(p2h)
        dp = [0] * (1 << n)
        dp[0] = 1

        for i in range(n):
            for h in p2h[i]:
                h2p[h-1].append(i)    
        
        for i in range(40):
            for j in range((1 << n) -1, -1, -1): # we want to go from everyone has hat to no one has hat
                print(bin(j))
                for p in h2p[i]: # people assigned to hat_i
                    if (j & 1 << p) == 0:
                        dp[j | 1 << p] += dp[j]
        
        return dp[-1] % (10**9 + 7)
