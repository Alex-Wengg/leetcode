# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(parent, root):
            nonlocal cnt
            if root is None:
                return False
            if root.val >= parent:
                cnt += 1

            dfs(max(parent, root.val), root.right)
            dfs(max(parent, root.val), root.left)

        dfs(root.val, root)
        return cnt