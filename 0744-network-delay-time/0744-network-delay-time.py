from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        map = defaultdict(list)

        for x,y,z in times:
            map[x].append((y,z))

        greater = []
        pq = [(0, k)]

        resolved = [0] * (n+1)
        ret = 0 

        while pq:
            d, cur = heapq.heappop(pq)

            if resolved[cur]:
                continue
            
            resolved[cur] = 1
            ret = max(ret, d)

            for next, weight in map[cur]:
                if resolved[next]:
                    continue
                heapq.heappush(pq, (d+weight, next))

        for i in range(1, n+1):
            if resolved[i] == 0:
                return -1
        return ret