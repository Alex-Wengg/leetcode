# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")
        def helper(node):
            nonlocal res
            if node is None:
                return 0
            
            left = max(helper(node.left), 0 )
            right = max(helper(node.right), 0)

            res = max(res, left+right+node.val)
            
            return node.val + max(left, right)
        helper(root)
        return res