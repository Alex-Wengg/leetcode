from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        map = defaultdict(list)

        for x,y,z in times:
            map[x].append((y,z))

        dist = [float('inf')] * (n + 1)
        seen = [0] * (n+1)
        dist[k] = 0

        for i in range(1, n+1):
            minVal = float('inf')
            minNode = -1

            for j in range(1, n+1):
                if (not(seen[j]) and dist[j] < minVal):
                    minVal = dist[j]
                    minNode = j
                
            if minNode == -1:
                break
            
            seen[minNode] = 1
            for next, d in map[minNode]:
                dist[next] = min(dist[next], dist[minNode] + d)
            
        ret = 0
        for i in range(1, n+1):
            ret = max(ret, dist[i])
        return -1 if ret == float('inf')  else ret 