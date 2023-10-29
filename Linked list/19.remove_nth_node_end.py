# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        
        for i in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        temp = prev.next.next
        prev.next.next = None
        prev.next = temp
        return head