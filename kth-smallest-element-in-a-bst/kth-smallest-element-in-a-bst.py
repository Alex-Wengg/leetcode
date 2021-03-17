# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def printInorder(root,check): 
            if root: 
  
                check.append(root.val)
                printInorder(root.left,check) 

                printInorder(root.right,check) 
        check = []
        printInorder(root,check)
        check.sort()
        return check[k-1]