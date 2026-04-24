"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 2: one pass

        hashMap = defaultdict(lambda: Node(0)) # Key = original, val = copy
        hashMap[None] = None # Create a None to point to 

        start = head
        while head: # Only pass, using defaultdict with lambda to create new deepcopy node
                    # each time and update all values with original
            hashMap[head].val = head.val
            hashMap[head].next = hashMap[head.next]
            hashMap[head].random = hashMap[head.random]
            head = head.next

        return hashMap[start]
