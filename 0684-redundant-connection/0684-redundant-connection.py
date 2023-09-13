class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        def find(n):
            return find(par[n]) if par[n] != n else par[n]

        def union(p1, p2):
            p1 = find(p1)
            p2 = find(p2)

            if p1 <= p2:
                par[p2] = p1
            else:
                par[p1] = p2
            
        for x,y in edges:
            par[x] = x
            par[y] = y
        
        for x,y in edges:
            if find(x) == find(y):
                return [x, y]
            else:
                union(x, y)
        return edges[0]