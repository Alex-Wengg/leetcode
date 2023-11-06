class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        

        persons = [ [] for i in range(40)]
        n = len(hats)
        mod = 10 ** 9 + 7

        masks = [ 0 for i in range(1 << n)]
        masks[0] = 1

        for i in range(n):
            for h in hats[i]:
                persons[h-1].append(i)
        
        for i in range(40): # hats
            for j in range((1 << n) - 1, -1, -1): # people

                for p in persons[i]: 
                    if ((j & ( 1 << p)) == 0): # not assigned a hat yet
                        masks[ j | ( 1 << p)] += masks[j]
                        masks[ j | ( 1 << p)] %= mod
        
        return masks[-1]