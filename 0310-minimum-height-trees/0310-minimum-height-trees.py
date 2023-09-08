
def bfs_shortest_path(src, V, graph):
        # Distance array initialized to infinite distances
        dist = [float("inf")] * V
        dist[src] = 0

        # Use a queue for BFS
        q = deque([src])

        while q:
            u = q.popleft()

            # Iterate over neighboring vertices
            for v in graph[u]:
                if dist[v] == float("inf"):
                    dist[v] = dist[u] + 1  # Increment distance by 1 since all edges have the same weight
                    q.append(v)
        max_ =max(dist)
        return max_  

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (n==1): return [0]
        if (n==2): return [0,1]
        next = [[] for i in range(n)]
        degree = [ 0 for i in range(n)]

        
        for x, y in edges:
            degree[x] += 1
            degree[y] += 1
            next[x].append(y)
            next[y].append(x)

        q = []
        visited = [0 for i in range(n)]

        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        
        count = 0
        while q:
            size = len(q)
            while size:
                size -= 1
                cur = q.pop(0)
                count += 1
                visited[cur] = 1

                for nxt in next[cur]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        q.append(nxt)
            
            if (count == n - 1 or count == n -2):
                break

        
        res = []
        for i in range(n):
            if visited[i] == 0:
                res.append(i)
        return res 