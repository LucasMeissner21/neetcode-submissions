# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Attempt 1, reverse in place and track previous tail, current head
        # Every k reversed nodes, set previous tail to point to current head and checks
        # that at least k more nodes exist. If not, appends rest of nodes and returns
        start = None
        prev = None
        headC = head  # head of current group (before reversal, becomes tail after)
        tailP = None  # tail of previous reversed group
        n = 0

        while head:
            # Reverse nodes
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
            n += 1

            if n == k:
                # prev is now the new head of the reversed group
                # headC is now the tail of the reversed group

                if start is None:
                    start = prev  # first group, set start
            
                if tailP is not None:
                    tailP.next = prev  # connect previous group's tail to current group's new head

                tailP = headC  # headC becomes the tail after reversal
                headC = head   # next group starts at current head

                # lookahead: check if k nodes remain
                check, count = head, 0
                while check and count < k:
                    check = check.next
                    count += 1
                if count < k:
                    tailP.next = head  # attach remaining nodes as-is
                    return start

                prev = None
                n = 0

        return start