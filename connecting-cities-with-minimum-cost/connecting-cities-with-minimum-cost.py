class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        '''
        prim's algorithm
        1. initalize a tree with a vertex
        2. grow tree edge with smallest branch and connect it to the vertex
        3. repeat
        '''
        G = collections.defaultdict(list)
        
        for city1, city2, cost in connections:
            G[city2].append((cost, city1))
            G[city1].append((cost, city2))            
        
        queue = [(0,N)]
        visited = set()
        total = 0
        
        while queue and len(visited) < N :
            #PST uses pq and greedy algorithm
            cost, city = heapq.heappop(queue)
            #standard dfs stuff on graphs
            if city not in visited:
                visited.add(city)
                total += cost
                #add to pq 
                for cost, next_city in G[city]:
                    heapq.heappush(queue, (cost, next_city))
        return total if len(visited) == N else -1 