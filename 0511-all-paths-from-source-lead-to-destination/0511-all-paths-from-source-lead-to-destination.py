class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            
        visited = [ 0 for _ in range(n)]

        def dfs(i):
            if len(graph[i]) == 0:
                return i == destination
            elif visited[i] in  [1, 2]:
                return visited[i] == 2
            else:
                visited[i] = 1
                for nei in graph[i]:
                    if not dfs(nei):
                        return False
                
                visited[i] = 2
                return True 
            
        return dfs(source)