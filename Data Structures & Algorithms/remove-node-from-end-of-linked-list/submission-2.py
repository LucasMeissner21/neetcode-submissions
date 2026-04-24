# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution 1
        start = head
        i = 0
        while head: # Step through head to get number of nodes
            i += 1
            head = head.next
        if i == 1: # If only 1 node, only outcome is no nodes
            return None

        head = start
        i = i - n

        if i == 0: # If i = 0, removing first node, return second
            return start.next

        prev = None
        while i > 0: # Step until node to be removed
            prev = head
            head = head.next
            i -= 1

        # Link nodes around removed and return
        prev.next = head.next
        return start