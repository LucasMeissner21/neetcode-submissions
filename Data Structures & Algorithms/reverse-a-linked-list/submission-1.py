# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head: # Iterate through and reverse the list as you go in one pass
            next_node = head.next
            head.next = previous
            previous = head
            head = next_node
        return previous