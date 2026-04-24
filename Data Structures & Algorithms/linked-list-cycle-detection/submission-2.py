# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowP, fastP = head, head
        if not slowP:
            return False
        while fastP:
            slowP = slowP.next
            if fastP.next:
                fastP = fastP.next
            else:
                return False
            if fastP.next:
                fastP = fastP.next
            else:
                return False
            if slowP == fastP:
                return True
        return False