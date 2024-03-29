class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        graph = [[] for i in range(n+1)]
        seen = [0] * (n+1)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(i ,t):
            if i != 1 and len(graph[i]) == 1 or t == 0:
                return i == target
            
            seen[i] = 1
            res = sum(dfs(j, t- 1) for j in graph[i] if not seen[j])
            return res * 1.0 / (len(graph[i]) - (i != 1))
        return dfs(1, t)