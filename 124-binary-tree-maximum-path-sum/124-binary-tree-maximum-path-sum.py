# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        def helper(node):
            nonlocal res
            if node == None:
                return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            
            res = max(res, left+right+node.val)
            
            return max(left,right) + node.val
        helper(root)
        return res