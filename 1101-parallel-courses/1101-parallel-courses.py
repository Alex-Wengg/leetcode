class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        


        vDepth = [1] * n
        visitState = [0] * n
        g = [[] for i in range(n)]
        def dfs(i):
            if visitState[i] != 0 :
                return visitState[i] == 1
            
            visitState[i] = -1
            for j in g[i]:
                if not(dfs(j)):
                    return False
                vDepth[i] = max(vDepth[i], 1 + vDepth[j])
            visitState[i] = 1
            return True 
        
        for v in relations:
            g[v[0] - 1].append(v[1] - 1)

        for i in range(n):
            if not(dfs(i)):
                return -1
        return max(vDepth)