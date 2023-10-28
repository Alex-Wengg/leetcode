class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
    
        # Create the graph from the edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        shortest = float('inf')

        # BFS from each vertex
        for start in range(n):
            visited = {}
            # Each entry in the queue is a (vertex, parent, depth) tuple
            queue = deque([(start, None, 0)])
            
            while queue:
                node, parent, depth = queue.popleft()
                
                if node in visited:
                    # When a node is revisited, it means a cycle has been found
                    # The current depth minus the depth when it was first visited is the cycle length
                    shortest = min(shortest, depth +  visited[node])
                else:
                    visited[node] = depth
                    for neighbor in graph[node]:
                        if neighbor != parent:  # Don't go back immediately to the parent
                            queue.append((neighbor, node, depth + 1))
        
        if shortest == float('inf'):
            return -1
        else:
            return shortest 
