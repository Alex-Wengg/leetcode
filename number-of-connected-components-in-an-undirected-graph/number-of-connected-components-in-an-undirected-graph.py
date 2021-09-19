class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(child, graph, visited):
            if visited[child]:
                return
            visited[child] = 1
            
            for offspring in graph[child]:
                dfs(offspring, graph, visited)
        visited = [0] * n
        graph = {i:[] for i in range(n)}
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        ret =0
        for x in range(n):
            if not visited[x]:
                dfs(x, graph, visited)
                ret += 1
        return ret