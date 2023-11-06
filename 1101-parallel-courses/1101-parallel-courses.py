class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        def dfs(i, g, vDepth, visitState):
            if visitState[i]  == 1:
                return True
            if visitState[i] == -1:
                return False
            
            visitState[i] = -1
            for j in g[i]:
                if not(dfs(j, g, vDepth, visitState)):
                    return False
                vDepth[i] = max(vDepth[i], 1 + vDepth[j])
            visitState[i] = 1
            return True 

        vDepth = [1] * n
        visitState = [0] * n
        g = [[] for i in range(n)]
        for v in relations:
            g[v[0] - 1].append(v[1] - 1)

        for i in range(n):
            if not(dfs(i, g, vDepth, visitState)):
                return -1
        return max(vDepth)