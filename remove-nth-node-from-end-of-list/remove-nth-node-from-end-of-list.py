# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = head
        size = 0
        
        while length:
            prev = length
            length =length.next
            size += 1     
        if size == n : return head.next
        for i in range(1, size -n):
            curr = curr.next
        curr.next = curr.next.next
        return head