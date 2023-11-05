class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
        visited = [0 for _ in range(n)]
        def dfs(i):
            if len(graph[i]) == 0:
                return i == destination
            elif visited[i] == 1:
                return False
            elif visited[i] == 2:
                return True
            else:
                visited[i] = 1
                for j in graph[i]:
                    if not dfs(j):
                        return False
                visited[i] = 2
                return True    

        return dfs(source)