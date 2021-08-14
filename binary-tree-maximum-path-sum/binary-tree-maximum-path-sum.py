# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]
        def helper(node):
            if node is None:
                return 0
            
            left = max(0 , helper(node.left))
            right = max(0, helper(node.right))
            
            res[0] = max(res[0], left+right+node.val)
            
            
            return max(left,right) + node.val
        helper(root)

        return res[0]