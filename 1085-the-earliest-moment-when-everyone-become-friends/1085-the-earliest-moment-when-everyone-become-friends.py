class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = [ i for i in range(n)] # startingout everyone their own parent
        friended = n -1 # just need n-1 edges for these vertices

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal friended
            x = find(x)
            y = find(y)
            if x != y:
                parent[x] =y 
                friended -=1
                return True
            return False
        logs.sort()
        for log, x, y in logs:
            if union(x, y) and friended == 0:
                return log
        return -1