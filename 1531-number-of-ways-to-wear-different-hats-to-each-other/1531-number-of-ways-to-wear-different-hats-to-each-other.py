class Solution:
    def numberWays(self, p2h: List[List[int]]) -> int:
        n = len(p2h)
        h2p = [ [] for i in range(40)]
        dp = [0 for i in range(1<<n)] # represents ways to give specific ppl hats
        dp[0] = 1

        for i in range(n):
            for h in p2h[i]:
                h2p[h - 1].append(i)
        
        for i in range(40): # loop each hat 
            for j in range((1<<n)-1, -1, -1): # loop each person combination, who has hat(1) / nohat(0)
                for p in h2p[i]: # for person in hat : personList
                    if (j & (1<<p)) == 0: # person_p no hat
                        dp[j | 1<<p ] += dp[j] # 
        
        return dp[-1] % (10**9 + 7)