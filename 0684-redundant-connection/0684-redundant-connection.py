class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        def find(n):
            return find(par[n]) if n != par[n] else par[n]

        def union(p1, p2):
            if p1 <= p2:
                par[p2] = p1
            else:
                par[p1] = p2

        par = {}
        for x,y in edges:
            par[x], par[y] = x, y
        for x,y in edges:
            if find(x) == find(y):
                return [x, y]
            union(find(x), find(y))
        return edges
