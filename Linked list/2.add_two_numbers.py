# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        first = l1
        second = l2
        ptr = ListNode(-1,None)
        head = ptr
        sum=0
        while first and second:
            if carry:
                sum = first.val+second.val + 1
                carry=0
            else: 
                sum = first.val+second.val
            if sum>9:
                carry = sum//10
                sum = sum%10
            first = first.next
            second = second.next
            node = ListNode(sum)
            ptr.next = node
            ptr = ptr.next
        while first:
            if carry:
                sum = first.val+1
                carry=0
            else: 
                sum = first.val
            if sum>9:
                carry = sum//10
                sum = sum%10
            node = ListNode(sum)
            ptr.next = node
            ptr = ptr.next
            first = first.next
        while second:
            if carry:
                sum = second.val+1
                carry=0
            else: 
                sum = second.val
            if sum>9:
                carry = sum//10
                sum = sum%10
            node = ListNode(sum)
            ptr.next = node
            ptr = ptr.next
            second = second.next
        if carry:
            node = ListNode(carry)
            ptr.next = node
            ptr = ptr.next
        return head.next
        