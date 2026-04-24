# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fastP = head
        slowP = head

        i = 0
        while fastP: # Slow/Fast pointer to get midpoint
            if i % 2:
                slowP = slowP.next
            fastP = fastP.next
            i += 1

        # l2 is list to be merged in reverse (second half), l1 is first half
        l2 = slowP.next
        slowP.next = None
        l1 = head
        
        # Reversing l2
        prev = None
        while l2:
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node
        l2 = prev

        # Merging lists
        while l2:
            next_l1 = l1.next
            next_l2 = l2.next
            l1.next = l2
            l2.next = next_l1
            l2 = next_l2
            l1 = next_l1
                

        
