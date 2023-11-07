class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        

        h2p = [ [] for i in range(40)]
        n = len(hats)
        mod = 10 ** 9 + 7

        dpPersonHatsAssigned = [ 0 for i in range(1 << n)]
        dpPersonHatsAssigned[0] = 1

        for i in range(n):
            for h in hats[i]:
                h2p[h-1].append(i)
        
        for i in range(40): # hats
            for j in range((1 << n) - 1, -1, -1): # people

                for p in h2p[i]: # assign person_y to hat_x
                    if ((j & ( 1 << p)) == 0): # not assigned a hat yet
                        dpPersonHatsAssigned[ j | ( 1 << p)] += dpPersonHatsAssigned[j] 
        
        return dpPersonHatsAssigned[-1]% mod