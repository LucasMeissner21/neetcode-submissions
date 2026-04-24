# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Second solution, greedy, set pointer to be n steps ahead. Once this pointer reaches
        # the end, the pointer from the start is at the one to be removed. One pass
        if not head.next:
            return None

        remove, end = head, head

        for i in range(n):
            end = end.next

        if not end:
            return head.next
        
        end = end.next
        while end:
            remove = remove.next
            end = end.next

        remove.next = remove.next.next
        return head