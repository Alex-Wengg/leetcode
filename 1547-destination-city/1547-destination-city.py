
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj = collections.defaultdict(list)

        for x, y in paths:
            adj[x].append(y)

        for x, y in paths:
            if y not in adj:
                return y 
        return ""