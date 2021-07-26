# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        mapp  = {}
        while fast != None:
            if fast  in mapp:
                return True  # found the cycle
            mapp[fast] = fast
            fast = fast.next
            
            
        return False