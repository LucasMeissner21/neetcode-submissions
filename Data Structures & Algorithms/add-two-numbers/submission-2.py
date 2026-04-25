# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Attempt 1, generate new list node of sums, pretty self explanatory
        res = ListNode(0)
        start = res
        carry = 0
        while l1 or l2:
            if not l1:
                val = l2.val + carry
            elif not l2:
                val = l1.val + carry
            else:
                val = l1.val + l2.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(val)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            res.next = ListNode(carry)

        return start.next
            
