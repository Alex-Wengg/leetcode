class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]

        for x,y in prerequisites:
            graph[x].append(y)
        result = []
        def dfs(i):
            if visited[i] == -1: # -1 for visited, grey cycle
                return False 
            if visited[i] == 1: # post grey cycle
                return True
            
            visited[i] = -1
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            visited[i] = 1
            result.append(i)

            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        return result