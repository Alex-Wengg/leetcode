"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        
        def dfs(currNode):
            if currNode.val in visited:
                return visited[currNode.val]

            temp = Node(currNode.val)
            visited[currNode.val] = temp

            for neighor in currNode.neighbors:
                temp.neighbors.append(dfs(neighor))
            
            return temp
        return dfs(node) if node else None