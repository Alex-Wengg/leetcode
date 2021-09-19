class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        print([110,1,2,3,4,5])
        ans = 0
        for i in range(N):
            print(i, A[i])
            
            if i not in seen:
                dfs(i)
                ans += 1
            print(seen)
       
        return ans