import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        next = defaultdict(list)

        for x,y,z in flights:
            next[x].append((y,z))

        cost = [[float('inf') for _ in range(k+2)] for _ in range(n)]

        pq = [(0 , src, 0)]

        while pq:
            c, cur, stops = heapq.heappop(pq)

            if cur == dst:
                return c 
            
            if stops == k + 1:
                continue

            if cost[cur][stops] < float('inf'):
                continue
            
            cost[cur][stops] = c

            for nxt, price in next[cur]:
                if cost[nxt][stops+1] < float('inf'):
                    continue
                heapq.heappush(pq, (c+price, nxt, stops+1))
        
        return -1 