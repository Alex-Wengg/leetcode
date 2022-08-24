# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwoList(curr1, curr2):
            
            list3 = ListNode()
            curr3 = list3
     
            while (curr1 != None and curr2 != None):
                if curr1.val > curr2.val:
                    curr3.next = curr2
                    curr2 = curr2.next
                else:
                    curr3.next = curr1
                    curr1 = curr1.next
                curr3 = curr3.next
            if curr1:
                curr3.next = curr1
            if curr2:
                curr3.next = curr2
            return list3.next
        
        while len(lists) != 1:
            list1 = lists.pop()
            list2 = lists.pop()
            
            lists.append(mergeTwoList(list1, list2))
        
        return lists[0]