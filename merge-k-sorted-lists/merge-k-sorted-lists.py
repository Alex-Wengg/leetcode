class Solution(object):
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        def mergeTwoLists(l1, l2):
            res = []
            dummy = ListNode()
            l3 = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    l3.next = l2
                    l2 = l2.next
                else:
                    l3.next = l1
                    l1 = l1.next
                l3 = l3.next
            if l1:
                l3.next = l1
            elif l2:
                l3.next = l2
            return dummy.next
        
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()  
            lists.append(mergeTwoLists(l1, l2))
        return lists[0]