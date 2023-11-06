class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:


        res = 0
        n = len(favorite)
        al = [ [ ] for i in range(n)]
        visited= [{} for i in range(100000)]

        def dfs(curr, adj):
            visited[curr] = True
            res = 0
            for x in adj[curr]:
                res = max(res, dfs(x, adj))
            return res + 1

        for i in range(n):
            if favorite[favorite[i]] != i:
                al[favorite[i]].append(i)
        
        for i in range(n):
            if favorite[favorite[i]] == i:
                res +=dfs(i, al)
        
        for i in range(n):
            cnt = 0
            j = i
            while not(visited[j]):
                visited[j] = True
                cnt += 1
                j = favorite[j]
        
            k = i
            while k != j:
                cnt -= 1
                k = favorite[k]
            res = max(res, cnt)
        
        return res