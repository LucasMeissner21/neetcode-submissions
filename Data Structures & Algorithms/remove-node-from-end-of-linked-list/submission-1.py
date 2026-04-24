# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        i = 0
        while head:
            i += 1
            head = head.next
        if i == 1:
            return None

        head = start
        i = i - n

        if i == 0:
            return start.next

        prev = None
        while i > 0:
            prev = head
            head = head.next
            i -= 1

        prev.next = head.next
        return start