class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def root(parent, i):
            if(parent[i] != i):
                parent[i] = root(parent, parent[i])
            return parent[i]
        n = len(edges)
        parent = [0] * (n+1)
        candA = []
        candB = []

        for edge in edges:
            if (parent[edge[1]] == 0):
                parent[edge[1]] = edge[0]
            else:
                candA = [parent[edge[1]], edge[1]]
                candB = edge.copy()
                edge[1] = 0
        
        for i in range(1, n+1):
            parent[i] = i
        
        for edge in edges:
            if (edge[1]==0):
                continue
            u = edge[0]
            v = edge[1]
            pu = root(parent, u)

            if pu == v:
                if not len(candA):
                    return edge
                return candA
            parent[v] = pu
        return candB