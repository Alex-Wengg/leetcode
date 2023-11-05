class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(1+n)]
        res = 0
        e1 = 0
        e2 = 0 

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
            # return parent[i] if i == parent[i] else find(parent[i])
        
        def union(x, y):
            x, y = find(x), find(y)
            if y == x:
                return 0
            parent[x] = y
            return 1


        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = parent[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1
        
        parent = root0
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == e2 == n -1 else - 1