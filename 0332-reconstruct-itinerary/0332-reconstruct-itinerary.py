from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map = defaultdict(list) # string , []str

        tickets = sorted(tickets)

        for x,y in tickets:
            map[x].append(y)
        path = []
        def dfs( start, path):
            while len(map[start]) > 0:
                nextStart = map[start].pop(0)
                dfs(nextStart, path)
            path.append(start)

        dfs("JFK", path)
        path = reversed(path)
        return path