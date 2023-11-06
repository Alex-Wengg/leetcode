class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * n
        g = [ set() for i in range(n)]

        for v in relations:
            g[v[0] - 1].add(v[1] - 1)
            indegree[v[1] - 1] += 1
        
        maxDepth = 0
        numStudied = 0
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(( i, 1 ))
        
        while q:
            numStudied += 1
            i, depth = q.pop(0)
            maxDepth = max(depth, maxDepth)
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append((j, depth + 1))
        return maxDepth if numStudied == n else - 1