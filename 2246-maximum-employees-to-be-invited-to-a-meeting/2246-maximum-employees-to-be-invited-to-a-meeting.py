class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        visited = [0 for i in range(n)]
        indegrees = [ 0 for i in range(n)]

        for i in range(n):
            indegrees[favorite[i]] += 1
        
        q = []
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
                visited[i] = 1
        
        dp = [0 for i in range(n)]
        while q:
            i = q.pop()
            j = favorite[i]
            dp[j] = max(dp[j], dp[i] + 1)
            indegrees[j] -= 1
            if indegrees[j] == 0:
                visited[j] = 1
                q.append(j)
        
        result = 0
        result2 = 0
        for i in range(n):
            if visited[i]:
                continue
            length = 0 
            j = i 
            while visited[j] == 0:
                visited[j] = 1
                length += 1
                j = favorite[j]

            if length == 2:
                result2 += 2 + dp[i] + dp[favorite[i]]
            else:
                result = max(result ,length)
        return max(result, result2)