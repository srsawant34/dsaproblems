# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        reshead = None
        p1 = list1
        p2 = list2
        
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        if p1.val>p2.val:
            res = p2
            p2 = p2.next
            reshead = res
        else: 
            res = p1
            p1 = p1.next
            reshead = res
        
        while p1 and p2:
            if p1.val<p2.val:
                res.next = p1
                res = res.next
                p1 = p1.next
            else:
                res.next = p2
                res = res.next
                p2 = p2.next
        p = p1 or p2
        while p:
            res.next = p
            p=p.next
            res = res.next
        return reshead