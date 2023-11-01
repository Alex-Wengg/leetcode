# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        max_depth = 0
        max_node = None
        def dfs(node, depth):
            nonlocal max_node
            nonlocal max_depth
            if not(node):
                return depth

            right = dfs(node.right, depth + 1)
            left = dfs(node.left, depth + 1)

            max_depth = max(left, right, max_depth)
            if right == max_depth and left == max_depth:
                max_node = node

            return max(right, left)
        dfs(root, 0)
        return max_node