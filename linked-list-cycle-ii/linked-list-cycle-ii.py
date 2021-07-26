# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        mapp  = {}
        while fast != None:
            if fast  in mapp:
                return fast  
            mapp[fast] = fast
            fast = fast.next
            
            
        return None