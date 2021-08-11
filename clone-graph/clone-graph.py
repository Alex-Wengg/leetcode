"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        
        def dfs(node):
            #if its already in the node, no need to check or connect
            if node in dic:
                return dic[node]
            #add to the dicc
            print('============')
            print(node.val )
            print("columns")
            for i in range (len(node.neighbors)):
                print(node.neighbors[i].val)
            print("-------------------------")
            
            
            
            copy = Node(node.val)
            
            dic[node] = copy
            #check its neighbors
            for neighbor in node.neighbors:
                #
                copy.neighbors.append(dfs(neighbor))
                      


            return copy
        
        return dfs(node) if node else None