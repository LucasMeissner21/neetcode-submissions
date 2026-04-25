# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)
        res = ListNode(0)
        start = res

        while True:
            minV = float('inf')
            minI = -1
            for i in range(k):
                if not lists[i]:
                    continue
                if minV > lists[i].val:
                    minV = lists[i].val
                    minI = i
            if minI == -1:
                return start.next
            res.next = ListNode(minV)
            lists[minI] = lists[minI].next
            res = res.next