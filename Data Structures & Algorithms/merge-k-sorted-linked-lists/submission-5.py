# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Attempt 2: merge 2 lists k - 1 times, no extra space
        if not lists:
            return None
        start = ListNode(0, lists[0])
        for i in range(1, len(lists)):
            res = start
            while res.next or lists[i]:
                if not res.next:
                    res.next = lists[i]
                    break
                if not lists[i]:
                    break
                if res.next.val < lists[i].val:
                    res = res.next
                else:
                    hold = res.next
                    res.next = lists[i]
                    lists[i] = lists[i].next
                    res.next.next = hold
        return start.next

