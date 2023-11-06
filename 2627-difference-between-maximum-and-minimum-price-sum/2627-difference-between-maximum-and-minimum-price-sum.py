class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [ [] for i in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ans = 0

        def dfs(now, pre):
            nonlocal ans
            cur_max = [price[now], 0]
            for nei in g[now]:
                if nei == pre:
                    continue
                sub = dfs(nei, now)
                ans = max(ans, cur_max[0] + sub[1])
                ans = max(ans, cur_max[1] + sub[0])
                cur_max[0] = max(cur_max[0], sub[0] + price[now])
                cur_max[1] = max(cur_max[1], sub[1] + price[now])
            
            return cur_max
        dfs(0, -1 )
        return ans