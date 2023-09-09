from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) # string, [](string, double)

        results = []

        for (x, y), z in zip(equations, values):
            graph[x].append([y, z])
            graph[y].append([x, 1.0/z])
        # ================================
        def dfs( start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)
            temp = -1.0
            for mid, sec in graph[start]:
                if mid in visited:
                    continue
                temp2 = dfs(mid, end, visited)
                if temp2 != -1.0:
                    temp = sec * temp2
                    break
            return temp

        for x,y in queries:
            if x not in graph or y not in graph:
                results.append(-1.0)
            elif x == y:
                results.append(1.0)
            else:
                visited = set()
                temp = dfs(x, y, visited)
                results.append(temp)
        
        return results