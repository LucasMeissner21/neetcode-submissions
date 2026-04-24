# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Second solution, greedy, set pointer to be n steps ahead. Once this pointer reaches
        # the end, the pointer from the start is at the one to be removed. One pass

        if not head.next: # If only 1 node, it has to be removed
            return None

        remove, end = head, head

        for i in range(n): # Go until nth node
            end = end.next

        if not end: # If end is past all nodes, first node is being removed
            return head.next
        
        end = end.next # Move to next node so remove is 1 behind 
        while end: # Iterate until remove is before node to be removed
            remove = remove.next
            end = end.next

        remove.next = remove.next.next # Link nodes around removed node and return
        return head