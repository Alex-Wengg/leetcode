from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)

        # 0 / 1
        colours = [-1 for i in range(len(graph))]

        for i in range(len(graph)):
            for node in graph[i]:
                adjList[i].append(node)

        visited = set()
        def dfs(value):
            

            for neighour in adjList[value]:
                # 2 cases, coloured or nah

                # if nah
                if colours[neighour] == -1:
                    colours[neighour] = int(colours[value] == 0) 
                    if dfs(neighour) == False:
                        return False
                else:
                    if colours[neighour] == colours[value]:
                        return False
            
            return True 
        for i in range(len(graph)):
            if not dfs(i):
                return False
        return True
                