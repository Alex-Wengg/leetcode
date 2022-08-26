# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        dummyNode = ListNode(0, head)
        prevGroup = dummyNode
        
        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
                
            nextGroup = kth.next
            prev = kth.next
            curr = prevGroup.next
            
            while curr != nextGroup:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummyNode.next
    def getKth(self, start, k):
        
        while k > 0 and start:
            start = start.next
            k -= 1
        return start
  