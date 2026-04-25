# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Attempt 3: use heap to consistently get min value
        if not lists:
            return None
        
        minHeap = [] # Use minheap to get min value in O(1) time
        start = ListNode(0) 
        res = start

        for i in range(len(lists)):
            # Store value, list index, and first node of each linkedlist in minheap
            heapq.heappush(minHeap, (lists[i].val, i, lists[i])) 
            

        while minHeap:
            # get min node
            next_node = heapq.heappop(minHeap)
            
            # Append to res
            res.next = next_node[2]
            res = res.next

            # Move linked list node onto next
            lists[next_node[1]] = lists[next_node[1]].next
            # If next value exists, push onto minheap
            if lists[next_node[1]]:
                heapq.heappush(minHeap, (lists[next_node[1]].val, next_node[1], lists[next_node[1]]))
        
        return start.next
            