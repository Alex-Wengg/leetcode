class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        inDegree = [0] * (n+1)
        for r in relations:
            g[r[0]].append(r[1])
            inDegree[r[1]] += 1
        
        q = []
        for i in range(1, n+1):
            if inDegree[i] == 0:
                q.append(i)

        semester = 0
        while q:
            sz = len(q)
            for i in range(sz):
                c = q.pop(0)
                n -= 1
                if c not in g:
                    continue
                for course in g[c]:
                    inDegree[course] -= 1
                    if inDegree[course] == 0:
                        q.append(course)
                del g[c]

            semester += 1
        return semester if n == 0 else -1