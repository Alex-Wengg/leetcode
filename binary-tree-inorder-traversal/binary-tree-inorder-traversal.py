# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
def path(journey, root):
    if root: 

        # First recur on left child 
        if (root.left):
            path(journey, root.left) 

        # then print the data of node 
        journey.append(root.val) 

        # now recur on right child 
        if (root.right):
            path(journey, root.right)
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        journey = []
        path(journey, root)
        return(journey)
        
