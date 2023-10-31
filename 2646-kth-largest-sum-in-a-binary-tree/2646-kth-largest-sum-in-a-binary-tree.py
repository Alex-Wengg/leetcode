# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            level_ = len(queue)
            current_sum = 0

            for i in range(level_):
                q = queue.pop(0)
                current_sum += q.val

                if q.right:
                    queue.append(q.right)
                if q.left:
                    queue.append(q.left)
            result.append(current_sum)
        
        result.sort()
        print(result)
        return result[len(result) - k ] if len(result) >= k else -1