# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Attempt 3: use heap
        if not lists:
            return None
        
        minHeap = []
        start = ListNode(0)
        res = start

        for i in range(len(lists)):
            heapq.heappush(minHeap, (lists[i].val, i, lists[i]))

        while minHeap:
            next_node = heapq.heappop(minHeap)
            
            res.next = next_node[2]
            res = res.next

            lists[next_node[1]] = lists[next_node[1]].next
            if lists[next_node[1]]:
                heapq.heappush(minHeap, (lists[next_node[1]].val, next_node[1], lists[next_node[1]]))
        
        return start.next
            