class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        graph = collections.defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
              
        def recur_fn(node,parent):
            curr = values[node]
            res = 0
            for child in graph[node]:
                res += recur_fn(child,node)  if child != parent else 0 
            return min(res,curr) if res != 0 else curr

        return  sum(values) - recur_fn(0,-1)