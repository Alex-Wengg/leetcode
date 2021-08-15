# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def valid(node, smaller, greater):
            if not node:
                return True
            if not (smaller <  node.val < greater):
                return False
            return valid(node.left,smaller, node.val ) and valid(node.right, node.val, greater)
        return valid(root, float("-inf"), float("inf"))
    